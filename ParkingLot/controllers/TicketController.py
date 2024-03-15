from datetime import datetime

from LLD.ParkingLot.controllers.SlotController import SlotController, SimpleSlotSearchStrategy
from LLD.ParkingLot.controllers.VehicleController import VehicleController
from LLD.ParkingLot.models.Floor import Floor
from LLD.ParkingLot.models.ParkingLot import ParkingLot
from LLD.ParkingLot.models.Slot import Slot
from LLD.ParkingLot.models.Ticket import Ticket
from LLD.ParkingLot.models.Vehicle import VehicleType


class TicketController:
    @staticmethod
    def find_slot(parking_lot: ParkingLot, vehicle_type: VehicleType) -> tuple[Floor, Slot]:
        slot_controller = SlotController(SimpleSlotSearchStrategy())
        floor, slot = slot_controller.search_slot(parking_lot, vehicle_type)
        return floor, slot

    @staticmethod
    def create_ticket(parking_lot: ParkingLot, reg_no, vehicle_type: VehicleType, color):
        booking_time = datetime.now()

        vehicle = VehicleController.create_vehicle(reg_no, vehicle_type, color)

        floor, slot = TicketController.find_slot(parking_lot, vehicle_type)

        if slot:
            slot.is_empty = False
            slot.vehicle = vehicle
            return Ticket(parking_lot, booking_time, floor, vehicle, slot)
        else:
            return None

    @staticmethod
    def unpark_vehicle(ticket: Ticket):
        ticket.checkout_time = datetime.now()
        slot = ticket.slot
        if slot:
            SlotController.empty_slot(slot)


