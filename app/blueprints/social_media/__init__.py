from flask import Blueprint

bp = Blueprint('social_media',__name__, url_prefix='')

from .import routes 