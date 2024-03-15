from LLD.ParkingLot.models.Vehicle import Vehicle


class VehicleController:
    @staticmethod
    def create_vehicle(reg_no, vehicle_type, color):
        vehicle = Vehicle(reg_no, vehicle_type, color)
        return vehicle
