



class ModelNotSupportError(Exception):
    def __init__(self, message = "The Model is not supported."):
        self.message = message
        super().__init__(self.message)

class IllegalInputError(Exception):
    def __init__(self, message = "The input is illegal"):
        self.message = message
        super().__init__(self.message)