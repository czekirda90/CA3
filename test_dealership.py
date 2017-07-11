import unittest

from DBS_dealership import *

# test the car functionality
class TestCar(unittest.TestCase):

	def test_car_mileage(self):
		self.car = Car()
		self.assertEqual(0, self.car.getMileage())
		self.car.move(15)
		self.assertEqual(15, self.car.getMileage())
		self.car.setMileage(45)
		self.assertEqual(45, self.car.getMileage())

	def test_car_make(self):
		self.car = Car()
		self.assertEqual('', self.car.getMake())
		self.car.setMake('Fiat')
		self.assertEqual('Fiat', self.car.getMake())

	def test_car_colour(self):
		self.car = Car()
		self.assertEqual('', self.car.getColour())
		self.car.paint('red')
		self.assertEqual('red', self.car.getColour())
		self.car.setColour('green')
		self.assertEqual('green', self.car.getColour())

	def test_car_engine_size(self):
		self.car = Car()
		self.assertEqual('', self.car.engineSize)
		self.car.engineSize = '2.0tdi'
		self.assertEqual('2.0tdi', self.car.engineSize)

	def test_petrol_car_fuel_injection(self):
		petrol_car = PetrolCar()
		self.assertEqual('multiply', petrol_car.getFuelInjection())
		petrol_car.setFuelInjection('direct')
		self.assertEqual('direct', petrol_car.getFuelInjection())
	
	def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())
		
	def test_diesel_car_numer_cylinders(self):
		diesel_car = DieselCar()
		self.assertEqual('', diesel_car.getNumberCylinders())
		diesel_car.setNumberCylinders(4)
		self.assertEqual(4, diesel_car.getNumberCylinders())
	
	def test_hybrid_car_cylinders(self):
		hybrid_car = HybridCar()
		self.assertEqual('plugin hybrid', hybrid_car.getCylinders())
		hybrid_car.setCylinders('')
		self.assertEqual('', hybrid_car.getCylinders())

 
	def test_dealership(self):
		
		self.dealership=Dealership()
				
		self.dealership.process_rental() 
		self.dealership.process_rental()
		
		
		
		
		
		
		
if __name__ == '__main__':
	unittest.main()
