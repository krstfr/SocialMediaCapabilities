from flask import render_template
from flask_login import login_required, current_user
from .import bp as social_media
from app.blueprints.auth.models import User

@social_media.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@social_media.route('/post/my_timeline', methods=['GET'])
@login_required
def my_timeline():
    return render_template('my_timeline.html.j2', posts=current_user.posts)

@social_media.route('/show_users', methods=['GET'])
@login_required
def show_users():
    users = User.query.all()
    return render_template('show_users.html.j2', users=users)