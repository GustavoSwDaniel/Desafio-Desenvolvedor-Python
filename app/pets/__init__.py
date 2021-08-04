from flask import Blueprint
from app.pets import models

bp = Blueprint('pets', __name__)

from app.pets import controller
