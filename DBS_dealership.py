#DBS Car Rental will rent cars to their customer. They have the potential to rent either petrol, diesel, electric, or hybrid cars.
#They have initially 40 cars in their rental pool made up of 50% petrol, 20% diesel, 10% electric and 20% hybrid.
#When a car is not rented it is available to the customer to rent.
#Once a car is rented the car is assigned to the customer, and removed from the rental pool.
#When the car is returned by the customer it is assigned back into the rental pool.
#If all 40 cars are rented out the rental function should return a message to the customer saying "Sorry nothing to rent, please try again"




# Define a class for my car

class Car(object):
	# implement the car object.
	#implement functions needed 
	
	def __init__(self):
		self.__colour = ''
		self.__make = ''
		self.__mileage = 0
		self.engineSize = ''

	def getColour(self):
		return self.__colour

	def getMake(self):
		return self.__make

	def getMileage(self):
		return self.__mileage

	def setColour(self, colour):
		self.__colour = colour

	def setMake(self, make):
		self.__make = make

	def setMileage(self, mileage):
		self.__mileage = mileage

	def paint(self, colour):
		self.__colour = colour
		return self.__colour

	def move(self, distance):
		self.__mileage = self.__mileage + distance
		return self.__mileage
	
#creating classes for four different types of cars with a function of my choice in it

class DieselCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberCylinders = ''

	def getNumberCylinders(self):
		return self.__numberCylinders

	def setNumberCylinders (self, numberCylinders):
		self.__numberCylinders = numberCylinders

class ElectricCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCells = 1
		
	def getNumberFuelCells(self):
		return self.__numberFuelCells

	def setNumberFuelCells (self, numberFuelCells):
		self.__numberFuelCells = numberFuelCells
	
		
		
class PetrolCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__fuelInjection = "multiply"

	def getFuelInjection(self):
		return self.__fuelInjection

	def setFuelInjection (self, fuelInjection):
		self.__fuelInjection = fuelInjection
		
class HybridCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__cylinders = "plugin hybrid"

	def getCylinders(self):
		return self.__cylinders

	def setCylinders (self,cylinders):
		self.__cylinders = cylinders

# rented cars will be assigned to the customer, hence the Customer(Car) class
class Customer(Car):
	
	def __init__(self):
		Car.__init__(self)

# creating separated Dealership class, which will use classes and functions above

class Dealership(object):
#creating lists
	def __init__(self):
		
		self.electric_cars = []
		self.petrol_cars = []
		self.diesel_cars = [] 
		self.hybrid_cars = []
		self.customer = []
	
	def create_current_stock(self):
		for i in range(4):
		   self.electric_cars.append(ElectricCar())
		for i in range(20):
		   self.petrol_cars.append(PetrolCar())
		for i in range(8): 
			self.diesel_cars.append(DieselCar())
		for i in range(8): 
			self.hybrid_cars.append(HybridCar())
		
			
	def stock_count(self):
		print 'Petrol cars in stock ' + str(len(self.petrol_cars))
		print 'Electric cars in stock ' + str(len(self.electric_cars))
		print 'Diesel cars in stock ' + str(len(self.diesel_cars))
		print 'Hybrid cars in stock ' + str(len(self.hybrid_cars))
		print 'Cars rented ' + str(len(self.customer))
	
	def rent(self, car_list, customer_list, amount):
		
		if len(str(car_list)) < amount:
			print ':( Not enough cars in stock. Please try again '
			return
		total = 0
		while total < amount:
		   customer_list.append(car_list.pop())
		   total = total + 1
	
	def return_car(self, car_list, customer_list, amount):
		
		total = 0
		while total < amount:
		   car_list.append(customer_list.pop())
		   total = total + 1
			
		
	def process_rental(self):
		answer = raw_input('what type would you like? Petrol, Diesel, Electric or Hybrid: ')
		amount = int(raw_input('How many would you like?: '))
		
		
		if answer == 'Petrol':
			self.rent(self.petrol_cars, self.customer, amount)
		if answer == 'Electric':
			self.rent(self.electric_cars, self.customer, amount)
		if answer == 'Diesel':
			self.rent(self.diesel_cars, self.customer, amount)
		if answer == 'Hybrid': 
			self.rent(self.diesel_cars, self.customer, amount)
				
		self.stock_count()
		
	def process_return(self):
		amount = len(self.customer)
		answer = raw_input('Would you like to return your car/cars? y/n ')
		if answer == "y":
			if len(self.electric_cars) < 4: 
				self.return_car(self.electric_cars, self.customer, amount)
			if len(self.petrol_cars) < 20: 
				self.return_car(self.petrol_cars, self.customer, amount)
			if len(self.diesel_cars) < 8: 
				self.return_car(self.diesel_cars, self.customer, amount)
			if len(self.hybrid_cars) < 8: 
				self.return_car(self.hybrid_cars, self.customer, amount)
		self.stock_count()

#print out the menu with options
print "Welcome to the DBS Car Dealership. Best cars in the country for a bargain!" 
proceed = raw_input("Please choose one of the following options: \n 1.Car Rental \n 2.Car Return\n ")

#create the loops so the program executes
dealership = Dealership()
dealership.create_current_stock()

while proceed == '1':
	dealership.process_rental()
	proceed = raw_input('Shall we continue? y/n ')
	if proceed == 'n': 
		print "Bye!"
		
proceed = '2' 
while proceed == '2':
	dealership.process_return()
	proceed = raw_input('Shall we continue? y/n ')
	if proceed == 'n': 
		print "Bye!"
	
	
		
		


		
