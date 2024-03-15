from abc import ABC, abstractmethod

from LLD.ParkingLot.controllers.SlotController import SlotController
from LLD.ParkingLot.models.Floor import Floor
from LLD.ParkingLot.models.Vehicle import VehicleType


class FloorSetupStrategy(ABC):
    @abstractmethod
    def setup_slots(self, floor, num_slots):
        pass


class SimpleFloorSetupStrategy(FloorSetupStrategy):
    def setup_slots(self, floor, num_slots):
        for i in range(num_slots):
            if i == 0:
                floor.slots.append(SlotController.create_slot(i + 1, VehicleType.TRUCK))
            elif 1 <= i <= 2:
                floor.slots.append(SlotController.create_slot(i + 1, VehicleType.BIKE))
            else:
                floor.slots.append(SlotController.create_slot(i + 1, VehicleType.CAR))


class FloorController:
    def __init__(self, strategy: FloorSetupStrategy):
        self.strategy = strategy

    def create_new_floor(self, num, num_slots: int):
        floor = Floor(num)
        self.strategy.setup_slots(floor, num_slots)
        return floor

    @staticmethod
    def add_new_slot(floor, slot):
        floor.slots.append(slot)
