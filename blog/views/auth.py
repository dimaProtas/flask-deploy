from sqlite3 import IntegrityError
from flask import Blueprint, redirect, url_for, render_template, request, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.exceptions import NotFound

from blog.forms.user import RegisterForm, LoginForm
from blog.models import User
from blog.models.database import db

auth = Blueprint('auth', __name__, url_prefix='/auth', static_folder='../static')


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def login():
    return "WIP"
# if request.method == "GET":
# return render_template("auth/login.html")
#
#
# login_user(user)
# return redirect(url_for("index"))


@auth.route("/login-as/", methods=["GET", "POST"], endpoint="login-as")
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        # non-admin users should not know about this feature
        raise NotFound
    if request.method == 'GET':
        return render_template('auth/login-as.html')

    username = request.form.get('username')
    if not username:
        return render_template('auth/login-as.html', error='username nit passed')

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template('auth/login-as.html', error=f'no user {username!r} found')

    login_user(user)
    return redirect(url_for('index.index'))


@auth.route('/register/', methods=['GET', 'POST'], endpoint='register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))

    error = None
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template("auth/register.html", form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff = False,
        )
        user.password = form.password.data
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exeption("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("User created %s", user)
            login_user(user)
            return redirect(url_for('index.index'))

    return render_template('auth/register.html', form=form, error=error)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


@auth.route('/login/', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()

        if user is None:
            return render_template('auth/login.html', form=form, error='username does not exist!')

        if not user.validate_password(form.password.data):
            return render_template('auth/login.html', form=form, error='invalid username or password!')

        login_user(user)
        return redirect(url_for('index.index'))

    return render_template('auth/login.html', form=form)



@auth.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))


@auth.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"


__all__ = [
    'login_manager',
    'auth',
]
