from flask import jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from app.commons import bp


@bp.app_errorhandler(HTTPException)
def handle_error(e):
    return jsonify(error=e.description), e.code


@bp.app_errorhandler(Exception)
def handle_error(e):
    code = 500
    return jsonify(error=str(e)), code


@bp.app_errorhandler(ValidationError)
def handle_error(e):
    response = {
        'message': 'Some fields failed at validation',
        'fields': e.messages
    }
    return jsonify(response), 400
