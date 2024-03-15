from enum import Enum


class VehicleType(Enum):
    TRUCK = 'Truck'
    CAR = 'Car'
    BIKE = 'Bike'


class Vehicle:
    def __init__(self, registration_number: str, vehicle_type: VehicleType, color: str):
        self._vehicle_type = vehicle_type
        self._registration_number = registration_number
        self._color = color

    @property
    def registration_number(self):
        return self._registration_number

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @property
    def color(self):
        return self._color
    
