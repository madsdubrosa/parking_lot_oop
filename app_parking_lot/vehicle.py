
class Vehicle:
    acceptable_types = ["bike", "car", "bus"]

    def __init__(self, license_plate, color, vehicle_type):
        self.license_plate = license_plate
        self.color = color
        self.vehicle_type = vehicle_type if vehicle_type in self.acceptable_types else "car"
        self.parking_spot_number = None

    def buy_parking_spot(self, cost):
        # api calls to authenticate the transaction
        # have confirmation of the transaction
        print("Successful Transaction")
        return cost

    def park(self, parking_spot_number):
        self.parking_spot_number = parking_spot_number

    def leave_parking_spot(self):
        self.parking_spot_number = None
