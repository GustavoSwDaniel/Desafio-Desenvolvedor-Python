from flask import Blueprint

bp = Blueprint('common', __name__)

from app.commons import exceptions, error_handlers
