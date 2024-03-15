import unittest

from LLD.ParkingLot.controllers.ParkingLotController import ParkingLotController
from LLD.ParkingLot.controllers.SlotController import SlotController, SimpleSlotSearchStrategy
from LLD.ParkingLot.models.Vehicle import VehicleType


class TestSlotController(unittest.TestCase):
    def test_search_slot(self):
        parking_lot_controller = ParkingLotController()
        parking_lot = parking_lot_controller.add_parking_lot(3, 12)
        slot_controller = SlotController(SimpleSlotSearchStrategy())
        floor, slot = slot_controller.search_slot(parking_lot, VehicleType.CAR)
        self.assertEqual(floor.floor_num, 1)
        self.assertEqual(slot.slot_num, 4)
