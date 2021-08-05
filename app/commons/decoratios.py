import mimetypes

from functools import wraps
from flask import request
from werkzeug.exceptions import abort


def validate_image_file(function):
    @wraps(function)
    def verify_file(*args, **kwargs):
        types_not_accepted = [mimetypes.types_map['.exe'], mimetypes.types_map['.html'], mimetypes.types_map['.zip'],
                              mimetypes.types_map['.json'], mimetypes.types_map['.js'], 'application/x-msdos-program',
                              mimetypes.types_map['.sh'], mimetypes.types_map['.dll'], mimetypes.types_map['.py'],
                              mimetypes.types_map['.xml'], mimetypes.types_map['.css'], 'text/x.typescript',
                              'application/x-rar-compressed', 'application/bat', 'application/x-bat',
                              'application/textedit', 'application/octet-stream']

        file_mimetype = request.files.get('file').mimetype

        if file_mimetype is None or file_mimetype in types_not_accepted:
            message = 'The file is required. Not accepted types are ' + str(types_not_accepted)
            abort(422, message)
        else:
            return function(*args, **kwargs)

    return verify_file
