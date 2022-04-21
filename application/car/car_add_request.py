class CarAddRequest:
    def __init__(self, body) -> None:
        self.model = body['model']
        self.regNum = body['regNum']
