from pprint import pprint

from parking_lot_oop.app_parking_lot.parking_lot import ParkingLot
from parking_lot_oop.app_parking_lot.vehicle import Vehicle


def main():
    lot = ParkingLot()
    # bikes
    bike_1 = Vehicle("VR00MVR00M", "black", "bike")
    bike_2 = Vehicle("2FAST4U", "black", "bike")
    bike_3 = Vehicle("OH NOOOOO", "black", "bike")
    # cars
    car_1 = Vehicle("JGQ7832", "black", "car")
    car_2 = Vehicle("DXY4379", "green", "car")
    car_3 = Vehicle("1234567", "red", "car")
    # buses
    bus_1 = Vehicle("MEGA BUSS", "blue", "bus")
    bus_2 = Vehicle("PARTY BUS", "blue", "bus")
    bus_3 = Vehicle("JUST BUST", "blue", "bus")

    lot.sell_spot(car_1, 365)
    lot.sell_spot(bike_1, 1)
    lot.sell_spot(bus_1, 30)
    lot.sell_spot(bus_2, 365)
    lot.sell_spot(bus_3, 1)

    for i in range(48):
        lot.sell_spot(Vehicle(f"{i}", "blue", "bike"), 1)

    lot.sell_spot(bike_2, 1)
    lot.extend_spot(bike_2.license_plate, 30)

    lot.bulk_empty_spots([str(i) for i in range(48)])


    pprint(lot.empty_spots)
    pprint(lot.parked_vehicles)
    print(lot.revenue)



main()
