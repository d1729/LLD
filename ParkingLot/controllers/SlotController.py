from abc import ABC, abstractmethod
from typing import Union

from LLD.ParkingLot.models.Floor import Floor
from LLD.ParkingLot.models.ParkingLot import ParkingLot
from LLD.ParkingLot.models.Slot import CarSlot, BikeSlot, TruckSlot, Slot
from LLD.ParkingLot.models.Vehicle import VehicleType


class SlotSearchStrategy(ABC):
    @abstractmethod
    def search_slot(self, parking_lot: ParkingLot, vehicle_type: VehicleType):
        pass


class SimpleSlotSearchStrategy(SlotSearchStrategy):
    def search_slot(self, parking_lot: ParkingLot, vehicle_type:VehicleType) -> Union[tuple[Floor, Slot], tuple[None, None]]:
        floors = parking_lot.floors
        floors.sort(key=lambda floor: floor.floor_num)

        for floor in floors:
            slots = floor.slots
            slots.sort(key=lambda slot: slot.slot_num)
            for slot in slots:
                if slot.slot_type == vehicle_type and slot.is_empty:
                    return floor, slot

        return None, None


class SlotController:
    def __init__(self, strategy: SlotSearchStrategy):
        self.strategy = strategy

    def search_slot(self, parking_lot:ParkingLot, vehicle_type: VehicleType):
        return self.strategy.search_slot(parking_lot, vehicle_type)

    @staticmethod
    def create_slot(slot_num: int, slot_type: VehicleType):
        if slot_type == VehicleType.CAR:
            return CarSlot(slot_num)
        elif slot_type == VehicleType.BIKE:
            return BikeSlot(slot_num)
        elif slot_type == VehicleType.TRUCK:
            return TruckSlot(slot_num)
        else:
            return None

    @staticmethod
    def empty_slot(slot: Slot):
        slot.vehicle = None
        slot.is_empty = True
