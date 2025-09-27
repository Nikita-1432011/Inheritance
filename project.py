class Vehicle:
   def __init__(self, name, mileage, capacity):
     self.name = name
     self.mileage = mileage
     self.capacity = capacity

   def fare(self):
    return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
     amount = super(). fare()
     amount += amount * 10 / 100
     return amount
    
School_bus = Bus ("School vevlo", 15, 60)
print("Total Bus fare is:", School_bus. fare())