from typing import Any


class CarAddCommand:
    def __init__(self, model, registration_number) -> None:
        self.model = model
        self.registration_number = registration_number

    def __str__(self) -> str:
        return self.__dict__.__str__()
