class Error:
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

    def serialize(self):
        return {
            "error": self.error,
            "status_code": self.status_code
        }