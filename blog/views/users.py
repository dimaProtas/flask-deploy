from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models import User
from typing import Dict
import requests

user_app = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')


@user_app.route('/', endpoint='list')
def users_list():
    users = User.query.all()
    return render_template('users/user_list.html', users=users)


@user_app.route('/<int:user_id>', endpoint='details')
def user_detail(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        return NotFound(f"User {user_id} does not exist!")
    if user.author:
        article_id = user.author.id
        count_articles_det: Dict = requests.get(f'http://127.0.0.1:5000/api/articles/{article_id}/event_get_articles_count/').json()
    else:
        count_articles_det = {'count': 'is not the author'}
    return render_template('users/details.html', user=user, count_articles_det=count_articles_det['count'],)
