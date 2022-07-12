"""
Brain storming
1) Parking Lot --> levels 1-4; level 1 is for annual passes, level 2 is for monthly passes, and levels 3 and 4 are for
    dailys
2) Vehicles --> bikes (1/2 spot), cars (1 spot), buses (2 spots)
3) ticketing/payment --> rates/time unit
4) keep track of capacity for all vehicles

Class Design:
Parking Lot
    --> fields:
        1) parked_vehicles: Map[license_plate, Spot] --> Map[str, ParkingSpot]
        2) empty_spots = Map[level, Map[vehicle_type, num_empty_spots]] --> Map[int, Map[str, int]
        3) have a number of certain spots on each level depending on the vehicle (partition it maybe?)
            Bikes: 0.25
            Cars: 0.50
            Buses: 0.25
    --> methods:
        1) sell_passes
        2) keep track of spots (to make sure it is not full)
    Nested class: Parking Spot
        --> fields:
            1) registered_vehicle: Vehicle
            2) spot_size: int
            3) cost
            4) time = 365 (or 1, 30, 90, etc)
            5) duration --> (start_time, end_time = start_time + time)
            6) owner/driver --> license plate
        --> methods:
            1) fill_spot()
            2) empty_spot()
            3) receive_payment() # pay for the spot
            4) renew() // extend_pass()

Vehicles
    --> fields:
    1) have space they take up
    --> methods:
    1) park
    2) pay for the parking pass
    3) leave
    4) needs to keep track of where the vechile is parked
    Bike
        --> fields:
        1) space they take up: 1/2 spot --> size
        --> methods:
    Car
        --> fields:
        1) space they take up: 1 spot --> size
        --> methods:
    Bus
        --> fields:
        1) space they take up: 2 spots --> size
        --> methods:
"""
