class Vehical:

      def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        
class Bus(Vehical):
            def __init__(self,brand,colour,name,max_speed,mileage):
                  self.brand = brand
                  self.colour = colour
                 
                  Vehical.__init__(self, name, max_speed, mileage)

School_bus = Bus("abc","white","School Volvo",180,12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage",School_bus.mileage)
            