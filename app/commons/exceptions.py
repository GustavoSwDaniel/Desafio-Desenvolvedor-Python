class BasicError(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


class ObjectDoesNotFoundError(BasicError):
    def __init__(self, code_status=404, message='Object does not found'):
        super().__init__(message)
        self.code_status = code_status
