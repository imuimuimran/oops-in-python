class Vehicle:
    def __init__(self, fare, seat):
        self.fare = fare
        self.seat = seat
    def vehicle_fare(self):
        total_fare = self.seat * 100
        return total_fare
        
class Bus(Vehicle):
    def __init__(self, fare, seat):
        super().__init__(fare, seat)
        
    def bus_fare(self):
        net_fare = self.vehicle_fare() + ((self.fare * self.seat) * 10) / 100
        return net_fare
        
        
vehicle1 = Vehicle(100, 50)
print("Total vehicle fare: ", vehicle1.vehicle_fare())
bus1 = Bus(100, 50)
print("Total bus fare: ", bus1.bus_fare())
        