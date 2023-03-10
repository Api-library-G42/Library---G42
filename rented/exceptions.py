class BlockedException(Exception):
    def __init__(self, message):
        self.message = message


class DisponibleException(Exception):
    def __init__(self, message):
        self.message = message
