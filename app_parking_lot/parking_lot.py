
import random
from datetime import date
from dateutil.relativedelta import relativedelta
random.seed(12)


class ParkingLot:
    prices = {"bike": {1: 10, 30: 8,  365: 6},
              "car":  {1: 20, 30: 16, 365: 12},
              "bus":  {1: 40, 30: 24, 365: 18}}

    def __init__(self, num_spots_per_level=100):
        self.levels = 4  # level 1: annual, level 2: monthly, level 3: daily, level 4: daily
        self.level_to_duration = {1: 365, 2: 30, 3: 1, 4: 1}  # [(1, 365), (2, 30), (3, 1), (4, 1)]
        self.level_size = num_spots_per_level
        self.empty_spots = {lev: {"bike": int(self.level_size * 0.25),
                                  "car": int(self.level_size * 0.5),
                                  "bus": int(self.level_size * 0.25)}
                            for lev in range(1, self.levels+1)}
        self.parked_vehicles = {}  # Map[license_plate, spot] --> Map[str, ParkingSpot]
        self.revenue = 0

    def _generate_spot(self, vehicle, duration, delta_days=0):
        vehicle_type = vehicle.vehicle_type
        levels = [l for l, d in self.level_to_duration.items() if d == duration]  # [1]; [2]; [3, 4]
        spot_level = None
        for level in levels:
            if level != 3:
                if self.empty_spots[level][vehicle_type] > 0:
                    self.empty_spots[level][vehicle_type] -= 1
                    spot_level = level
                else:
                    print("Lot is full.")
                    return
            else:  # level 3
                if self.empty_spots[level][vehicle_type] > 0:
                    self.empty_spots[level][vehicle_type] -= 1
                    spot_level = level
                    break
        return self.ParkingSpot(vehicle, duration, spot_level, delta_days)

    def sell_spot(self, vehicle, duration):
        """
        sell a spot given a vehicle trying to buy; keep track of empty spots (to make sure lot is not full)
        """
        # check to see if the vehicle already owns a spot
        if self.parked_vehicles.get(vehicle.license_plate):
            print("You already own a spot.")
            return
        # giving the spot up
        parking_spot = self._generate_spot(vehicle, duration)
        if not parking_spot:
            return
        # updated parked vehicles to include the vehicle parked
        self.revenue += parking_spot.payment
        self.parked_vehicles[vehicle.license_plate] = parking_spot

    def empty_spot(self, license_plate):
        spot = self.parked_vehicles.pop(license_plate, None)
        if not spot:
            print("Your vehicle does not have a spot.")
            return
        self.empty_spots[spot.level][spot.vehicle.vehicle_type] += 1
        spot.vehicle.leave_parking_spot()
        return

    def bulk_empty_spots(self, license_plates):
        for lp in license_plates:
            self.empty_spot(lp)
        return

    def extend_spot(self, license_plate, more_time):
        """
        case 1: original duration == more_time
            easy thing to do, keep the spot and get more money
        case 2: original duration != more_time ; ex: orig: annual, extended: monthly
            A) monthly spot is unavailable  --> ask if they wanna change duration, move to daily
                (what if the daily is also packed), or kick them out (we pick this one)
            B) monthly spot is available    --> move the spot over (aka just get the spot)
        """
        spot = self.parked_vehicles.get(license_plate)
        if not spot:
            print("Your vehicle does not have a spot.")
            return
        delta = spot.end_date - date.today()
        if delta.days > 1:
            print("You cant extend yet.")
            return
        if spot.duration == more_time:
            spot.end_date += relativedelta(days=more_time)
            spot.payment = spot.vehicle.buy_parking_spot(spot.cost)
            self.revenue += spot.payment
        else:
            # we vacate this spot because we move levels
            vehicle = spot.vehicle
            vehicle.leave_parking_spot()
            vehicle_type = vehicle.vehicle_type
            self.parked_vehicles.pop(license_plate)
            self.empty_spots[spot.level][vehicle_type] += 1
            new_spot = self._generate_spot(vehicle, more_time, delta.days)
            if not new_spot:
                return
            self.revenue += new_spot.payment
            self.parked_vehicles[license_plate] = new_spot

    class ParkingSpot:
        def __init__(self, vehicle, duration, level, time_left=0):
            self.vehicle = vehicle
            self.duration = duration
            self.level = level
            self.cost = ParkingLot.prices[self.vehicle.vehicle_type][self.duration] * self.duration
            self.start_date = date.today()
            self.end_date = self.start_date + relativedelta(days=self.duration + time_left)
            self.parking_spot_number = random.randint(1, 400)
            self.payment = self.vehicle.buy_parking_spot(self.cost)
            self.vehicle.park(self.parking_spot_number)



