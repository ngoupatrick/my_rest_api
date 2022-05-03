class ErrorModel:
    def __init__(self, error) -> None:
        self.code = error.code
        self.description = error.description
