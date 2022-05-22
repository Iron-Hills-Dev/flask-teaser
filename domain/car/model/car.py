class Car:
    def __init__(self, car_id, model, registration_number) -> None:
        self.id = car_id
        self.model = model
        self.registration_number = registration_number

    def to_dict(self):
        return self.__dict__
