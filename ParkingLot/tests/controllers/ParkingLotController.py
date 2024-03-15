import unittest

from LLD.ParkingLot.controllers.FloorController import FloorController, SimpleFloorSetupStrategy
from LLD.ParkingLot.controllers.ParkingLotController import ParkingLotController
from LLD.ParkingLot.controllers.TicketController import TicketController
from LLD.ParkingLot.models.Vehicle import VehicleType


class TestParkingLotController(unittest.TestCase):
    def test_add_parking_lot(self):
        controller = ParkingLotController()
        controller.add_parking_lot(2, 3)
        controller.add_parking_lot(3, 4)
        self.assertEqual(len(controller.parkingLots), 2)

    def test_remove_parking_lot(self):
        controller = ParkingLotController()
        controller.add_parking_lot(2, 3)
        parking_lot_2 = controller.add_parking_lot(3, 4)
        controller.remove_parking_lot(parking_lot_2)
        self.assertEqual(len(controller.parkingLots), 1)

    def test_add_floors_to_parking_lot(self):
        controller = ParkingLotController()
        floor_controller = FloorController(SimpleFloorSetupStrategy())
        parking_lot = controller.add_parking_lot(2, 3)
        floor1 = floor_controller.create_new_floor(3, 20)
        floor2 = floor_controller.create_new_floor(4, 25)
        controller.add_floor_to_parking_lot(parking_lot, floor1)
        controller.add_floor_to_parking_lot(parking_lot, floor2)
        self.assertEqual(len(parking_lot.floors), 4)

    def test_get_free_parking_lot_count(self):
        controller = ParkingLotController()
        parking_lot = controller.add_parking_lot(2, 3)
        res = controller.get_free_parking_lot_count(parking_lot, VehicleType.CAR)
        self.assertEqual(res[0][1], 0)

        parking_lot = controller.add_parking_lot(2, 30)
        res = controller.get_free_parking_lot_count(parking_lot, VehicleType.CAR)
        self.assertEqual(res[0][1], 27)

    def test_get_occupied_parking_lots(self):
        controller = ParkingLotController()
        parking_lot = controller.add_parking_lot(1, 5)
        TicketController.create_ticket(parking_lot, VehicleType.CAR, VehicleType.CAR)
        res = controller.get_occupied_parking_lots(parking_lot)
        self.assertEqual(len(res[0]), 2)
