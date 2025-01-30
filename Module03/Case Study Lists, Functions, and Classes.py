""" 
Alexander Cox
1/29/2024
Case Study Lists, functions and Class.py
has 2 classes 1 parent class of vehicles and 1 child class of Automobile
Accepts user input to get the type of vehicle the make, model, year, number of doors, and type of roof
Year, number of doors, and type of roof have input validatition to restrict user input

"""
class Vehicles:
    def __init__(self, vehicle_type: str):
        self.vehicle_type: str = vehicle_type # TODO car,truck, plane, boat or a broom stick
    def __str__(self):
        return self.vehicle_type
        
        
class Automobile(Vehicles):
    def __init__(self,vehicle_type, year:int , make:str, model:str, doors: int, roof: str):
        super().__init__(vehicle_type=vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors #TODO 2 or 4
        self.roof:str  = roof #TODO solid or sun
    def __str__(self):
        return (f"Vehicle Type: {super().__str__()}\n" +
                f"Year: {self.year}\n" +
                f"Make: {self.make}\n" +
                f"Model: {self.model}\n" +
                f"Doors: {self.doors}\n" +
                f"Roof: {self.roof}")
        
        
vehicle_type:str = input("What is your vehicle type: ")
year: str = input("What is the year of the car: ")
while (not(year.isdigit())):
    year = input("What is the year of the car: ")
    
year = int(year)
make: str = input("What is the make of the car: ")
model:str = input("What is your vehicle model: ")
doors: str = input("What is the number of doors(2 or 4): ")
while (doors != "4" and doors !="2"):
    doors: str = input("What is the number of doors(2 or 4): ")
doors = int(doors)
roof: str = input("What kind of roof does the car have (Sun or Solid): ")
while(roof.lower() !="solid" and roof.lower() != "sun"):
    roof: str = input("What kind of roof does the car have (Sun or Solid): ")
car = Automobile(vehicle_type = vehicle_type, year=year, make=make, model=model,doors=doors, roof=roof)
print(car)