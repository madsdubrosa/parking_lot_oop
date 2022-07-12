# parking_lot_oop

Parking lot designed using Object Oriented Design.

parking_lot.py contains the class definition of the parking lot as well as a parking spot. vehicle.py contains the class definition for different types of vechiles that would be parked in the parking lot (bikes, cars, buses). 

The Parking Lot class contains:
  1. 4 levels (Level 1 is for Annual Parking Pass holders, Level 2 is for Monthly Parking Pass holder, and Levels 3 & 4 are for Daily Parking Pass use)
  2. Each level has allocated spots for different vechile types (Bikes: 1/2 spot, Car: 1 spot, Bus: 2 spots)
  3. Ticketing/Payment system. For where API calls would be used, print statements are added to simulate the API call
  4. The ability to keep track of the current capacity of each level
  5. A nested parking spot class that would register the vehicle that is parked in that spot as well as the cost and  duration

The Vehicle class contains:
  1. Different types of vechiles that can park in the parking lot as well as the license plate information
  2. The ability to park, puchase a parking spot and leave a parking spot

test_parking_lot.py contains various test cases to assess the parking lot and vechile classes, prior to running the simulation. main.py runs the overall simulation of the parking lot.
