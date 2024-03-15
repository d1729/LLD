from LLD.ParkingLot.controllers.FloorController import FloorController, SimpleFloorSetupStrategy
from LLD.ParkingLot.models.Floor import Floor
from LLD.ParkingLot.models.ParkingLot import ParkingLot
from LLD.ParkingLot.models.Vehicle import VehicleType


class ParkingLotController:
    def __init__(self):
        self.parkingLots = []

    def add_parking_lot(self, floors: int, slots: int):
        new_parking_lot = ParkingLot()

        floor_controller = FloorController(SimpleFloorSetupStrategy())
        for i in range(floors):
            floor = floor_controller.create_new_floor(i + 1, slots)
            new_parking_lot.floors.append(floor)

        self.parkingLots.append(new_parking_lot)
        return new_parking_lot

    def remove_parking_lot(self, parking_lot: ParkingLot):
        try:
            self.parkingLots.remove(parking_lot)
        except ValueError:
            print('Parking Lot does not exist')

    def get_parking_lots(self):
        return self.parkingLots

    @staticmethod
    def get_floors(parking_lot: ParkingLot):
        return parking_lot.floors

    @staticmethod
    def add_floor_to_parking_lot(parking_lot: ParkingLot, floor: Floor):
        parking_lot.floors.append(floor)
        return floor

    @staticmethod
    def get_free_parking_lots(parking_lot: ParkingLot, vehicle_type: VehicleType):
        free_parking_lots = []
        floors = ParkingLotController.get_floors(parking_lot)
        floors.sort(key=lambda floor: floor.floor_num)

        for floor in floors:
            slots = list(filter(lambda slot: (slot.is_empty, slot.slot_type) == (True, vehicle_type), floor.slots))
            free_parking_lots.append((floor, slots))

        return free_parking_lots

    @staticmethod
    def get_free_parking_lot_count(parking_lot: ParkingLot, vehicle_type: VehicleType):
        free_parking_lots = ParkingLotController.get_free_parking_lots(parking_lot, vehicle_type)
        parking_lot_count = [(free_parking_lot[0], len(free_parking_lot[1])) for free_parking_lot in free_parking_lots]
        return parking_lot_count

    @staticmethod
    def get_occupied_parking_lots(parking_lot: ParkingLot):
        occupied_parking_lots = []
        floors = ParkingLotController.get_floors(parking_lot)
        floors.sort(key=lambda floor: floor.floor_num)

        for floor in floors:
            slots = list(filter(lambda slot: not slot.is_empty, floor.slots))
            occupied_parking_lots.append((floor, slots))

        return occupied_parking_lots

    @staticmethod
    def remove_floor_from_parking_lot(parking_lot: ParkingLot):
        try:
            parking_lot.floors.remove(parking_lot)
        except ValueError:
            print('Floor does not exist')
