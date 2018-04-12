from booking import *
from car import *
from admin_system import *
from customer import *
class rental_system():
    def __init__(self):
        self._customers=[]
        self._bookings=[]
        self._cars=[]
        self._payment=[]
    def make_a_booking(self, book):
        self._customers.append(book._customer_ID)
        self._bookings.append(book._booking_ID)
        self._cars.append(book._car_ID)
        self._payment.append(book._customer_ID)
    def display_match_cars(self, car):
        print(get_name(car))
        print(get_ID(car))
        print(car.model)

    def accept_payment(self, customer_ID):
        self._payment.remove(customer_ID)
    def confirmation(self,customer,car,booking):
    	print("\n")
    	print("email confirmation!!!")
    	print("customer name:%s " %  customer.name)
    	print("detail of car: carID: %s ,model: %s, registration: %s, status: %s" % (car._car_id,car._model, car._registration, car._status) )
    	print("period booked: %d" % booking._period )
    	print("total rental fee %d" % booking.get_netprice(car))
    	pass

