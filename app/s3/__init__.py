from flask import Blueprint

bp = Blueprint('S3', __name__)

from app.s3 import controller
