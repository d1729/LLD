from LLD.ParkingLot.models.Vehicle import VehicleType


class Slot:
    def __init__(self, slot_num, vehicle_type: VehicleType):
        self.slot_num = slot_num
        self.slot_type = vehicle_type
        self.is_empty = True
        self.vehicle = None


class CarSlot(Slot):
    def __init__(self, slot_num: int):
        super().__init__(slot_num, VehicleType.CAR)


class BikeSlot(Slot):
    def __init__(self, slot_num: int):
        super().__init__(slot_num, VehicleType.BIKE)


class TruckSlot(Slot):
    def __init__(self, slot_num: int):
        super().__init__(slot_num, VehicleType.TRUCK)
