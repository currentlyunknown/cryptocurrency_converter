from flask import jsonify

from settings import app


class CustomException(Exception):

    def __init__(self, message, status_code=400):
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv


@app.errorhandler(CustomException)
def handle_custom_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
