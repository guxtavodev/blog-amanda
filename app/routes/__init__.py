from flask import Blueprint, blueprints

artigos_bp = Blueprint('artigos', __name__)
comments_bp = Blueprint('comments', __name__)
admin_bp = Blueprint('admin', __name__)

from app.routes import artigos, comments, admin
