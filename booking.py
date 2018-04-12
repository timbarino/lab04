from customer import *
from car import *

class booking():
	def __init__(self, booking_ID, car, customer,location, period):
		self._booking_ID = booking_ID
		self._customer_ID = customer.customer_ID
		self._car_ID = car._car_id
		self._pickup_location = location
		self._period = period
        # compute rental fee
        #self._netprice = self._period * car._daily_fee
       

	def get_netprice(self,car):
		if car._model == "small" or car._model == "medium":
			netprice = self._period * car._daily_fee
		else:
			#print("case elase")		
			if (self._period > 7):
				netprice = 0.95 * self._period * car._daily_fee
				if car._model == "premium":
					netprice = 1.15 * netprice
		return netprice

