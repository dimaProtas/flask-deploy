from typing import Dict
from sqlite3 import IntegrityError

import requests
from flask import Blueprint, render_template, current_app, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.models.database import db
from blog.models import Author, Article, Tag
from blog.forms.article import CreateArticleForm

articles_app = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    count_articles: Dict = requests.get('http://127.0.0.1:5000/api/articles/event_get_count/').json()
    return render_template("articls/list.html", articles=articles, count_articles=count_articles['count'],)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id):
    article = Article.query.filter_by(id=article_id).options(joinedload(Article.tags)).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articls/details.html", article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)
        db.session.add(article)

        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles.details", article_id=article.id))
    return render_template("articls/create.html", form=form, error=error)
