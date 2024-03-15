import unittest

from LLD.ParkingLot.controllers.ParkingLotController import ParkingLotController
from LLD.ParkingLot.controllers.TicketController import TicketController
from LLD.ParkingLot.models.Vehicle import VehicleType


class TestTicketController(unittest.TestCase):
    def test_create_ticket(self):
        parking_lot_controller = ParkingLotController()
        parking_lot = parking_lot_controller.add_parking_lot(1, 10)
        ticket = TicketController.create_ticket(parking_lot, "TR01BT0348", VehicleType.CAR, "GREEN")
        self.assertEqual(ticket.slot.slot_num, 4)
        self.assertEqual(ticket.floor.floor_num, 1)
        self.assertFalse(ticket.slot.is_empty)
        self.assertIsNotNone(ticket.slot.vehicle)
        # print(ticket.ticket_id)
