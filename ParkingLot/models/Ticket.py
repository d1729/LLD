from datetime import datetime

from LLD.ParkingLot.models.ParkingLot import ParkingLot
from LLD.ParkingLot.models.Slot import Slot
from LLD.ParkingLot.models.Vehicle import Vehicle
from LLD.ParkingLot.models.Floor import Floor


class Ticket:
    def __init__(self, parking_lot: ParkingLot, booking_time: datetime, floor: Floor = None, vehicle: Vehicle = None,
                 slot: Slot = None):
        self._parking_lot = parking_lot
        self._booking_time = booking_time
        self._assigned_vehicle = vehicle
        self._floor = floor
        self._slot = slot
        self.checkout_time = None
        self._ticket_id = f"{str(self._parking_lot.id)}_{self._floor.floor_num}_{self._slot.slot_num}"

    @property
    def parking_lot(self):
        return self._parking_lot

    @parking_lot.setter
    def parking_lot(self, parking_lot: ParkingLot):
        self._parking_lot = parking_lot

    @property
    def booking_time(self):
        return self._booking_time

    @property
    def assigned_vehicle(self):
        return self._assigned_vehicle

    @assigned_vehicle.setter
    def assigned_vehicle(self, vehicle: Vehicle):
        self._assigned_vehicle = vehicle

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor: Floor):
        self._floor = floor

    @property
    def slot(self):
        return self._slot

    @slot.setter
    def slot(self, slot: Slot):
        self._slot = slot

    @property
    def ticket_id(self):
        return self._ticket_id
