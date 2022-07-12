from unittest import TestCase

from test_applications.oop.app_parking_lot.parking_lot import ParkingLot
from test_applications.oop.app_parking_lot.vehicle import Vehicle


class Test_Parking_Lot(TestCase):
    def setUp(self):
        self.lot = ParkingLot()

    def test_bike_spot(self):
        bike_1 = Vehicle("VR00MVR00M", "black", "bike")
        self.lot.sell_spot(bike_1, 1)
        self.assertEqual(self.lot.revenue, 10)
        self.assertEqual(self.lot.empty_spots[3]["bike"], 24)
        self.assertEqual(bike_1.parking_spot_number, self.lot.parked_vehicles[bike_1.license_plate].parking_spot_number)
        self.lot.empty_spot(bike_1.license_plate)
        self.assertTrue(bike_1.parking_spot_number is None)

    def test_extend_spot(self):
        bike_1 = Vehicle("VR00MVR00M", "black", "bike")
        self.lot.sell_spot(bike_1, 1)
        self.assertEqual(self.lot.revenue, 10)
        self.assertEqual(self.lot.empty_spots[3]["bike"], 24)
        self.assertEqual(bike_1.parking_spot_number, self.lot.parked_vehicles[bike_1.license_plate].parking_spot_number)
        self.lot.extend_spot(bike_1.license_plate, 30)
        self.assertEqual(self.lot.revenue, 250)
        self.assertEqual(self.lot.empty_spots[2]["bike"], 24)
        self.assertEqual(self.lot.empty_spots[3]["bike"], 25)
        self.assertEqual(bike_1.parking_spot_number, self.lot.parked_vehicles[bike_1.license_plate].parking_spot_number)

    def test_car_spot(self):
        car_1 = Vehicle("JGQ7832", "black", "car")
        self.lot.sell_spot(car_1, 365)
        self.assertEqual(self.lot.revenue, 4380)
        self.assertEqual(self.lot.empty_spots[1]["car"], 49)
        self.assertEqual(car_1.parking_spot_number, self.lot.parked_vehicles[car_1.license_plate].parking_spot_number)

    def test_bus_spot(self):
        bus_1 = Vehicle("MEGA BUSS", "blue", "bus")
        self.lot.sell_spot(bus_1, 1)
        self.assertEqual(self.lot.revenue, 40)
        self.assertEqual(self.lot.empty_spots[3]["bus"], 24)
        self.assertEqual(bus_1.parking_spot_number, self.lot.parked_vehicles[bus_1.license_plate].parking_spot_number)

    def test_flooring(self):
        for i in range(48):
            self.lot.sell_spot(Vehicle(f"{i}", "blue", "bike"), 1)
        self.assertEqual(self.lot.revenue, 480)
        self.assertEqual(self.lot.empty_spots[3]["bike"], 0)
        self.assertEqual(self.lot.empty_spots[4]["bike"], 2)
        self.lot.bulk_empty_spots([str(i) for i in range(48)])
        self.assertEqual(self.lot.empty_spots[3]["bike"], 25)
        self.assertEqual(self.lot.empty_spots[4]["bike"], 25)

    def test_annual_availability(self):
        for i in range(26):
            self.lot.sell_spot(Vehicle(f"{i}", "blue", "bike"), 365)
        self.assertEqual(self.lot.revenue, 54750)
        self.assertEqual(self.lot.empty_spots[1]["bike"], 0)
        self.assertEqual(len(self.lot.parked_vehicles), 25)

    def test_monthly_availability(self):
        for i in range(26):
            self.lot.sell_spot(Vehicle(f"{i}", "blue", "bike"), 30)
        self.assertEqual(self.lot.revenue, 6000)
        self.assertEqual(self.lot.empty_spots[2]["bike"], 0)
        self.assertEqual(len(self.lot.parked_vehicles), 25)



