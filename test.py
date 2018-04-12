from car import *
from admin import *
from admin_system import *
from customer import *
from booking import *
from insurance import*
from location import*
from rental_system import *

print("\n")
admin_1 = Admin("kirito","A001","kirito","666666")
print("Admin user name:",admin_1.get_user_name())
print("Admin password:",admin_1.get_pass_word())

AdminSystem = Admin_system()

AdminSystem.add_admin(admin_1)

print("password check:",AdminSystem.check_user_name("kirito","666666"))

print("\n")

print("The First Customer")
customer_1 = Customer("C001","tim","L123456","tim@gmail.com",18)
print("Customer ID:",customer_1.get_customer())
print("Customer Name:",customer_1.get_name())
print("Customer License:",customer_1.get_license())
print("Customer E-mail:",customer_1.get_email())
print("Customer age: ", customer_1.get_age())


print("\n")

location_1 = Location("darling harbour", "maroubra")
print("Pick up location:", location_1.get_pick_up())
print("Drop off location:", location_1.get_drop_off())

print("The Second Customer")
customer_2 = Customer("C002","customer 2", "L222222","c2@gmail.com",28)
print("Customer ID:",customer_2.get_customer())
print("Customer Name:",customer_2.get_name())
print("Customer License:",customer_2.get_license())
print("Customer E-mail:",customer_2.get_email())
print("Customer age: ", customer_2.get_age())

print("\n")

location_2 = Location("the start location", "the end location")
print("Pick up location:", location_2.get_pick_up())
print("Drop off location:", location_2.get_drop_off())



print("\n")

car_1 = small_car("reg1","small","carid1","good")
car_2 = medium_car("reg1","medium","carid2","good")
car_3 = large_car("reg1","large","carid3","good")
car_4 = premium_car("reg1","premium","carid4","bad")
print("All the car's status: car_1: %s, car_2: %s, car_3: %s, car_4: %s, " % (car_1._status,car_2._status,car_3._status,car_4._status))
system_1 = rental_system()
booking_1 = booking(1, car_1 ,customer_1,"location 1",12)
booking_2 = booking(2, car_2, customer_1,"location 2", 5)
booking_3 = booking(3, car_3, customer_1,"location 3", 10)
booking_4 = booking(4, car_4, customer_2,"location 4", 14)
print("fee for booking small car with 12 days:",booking_1.get_netprice(car_1))
print("fee for booking medium car with 5 days:",booking_2.get_netprice(car_2))
print("fee for booking large car with 10 days:",booking_3.get_netprice(car_3))
print("fee for booking premium car with 14 days:",booking_4.get_netprice(car_4))
print("\n")

system_1.make_a_booking(booking_1)
system_1.make_a_booking(booking_2)
system_1.make_a_booking(booking_3)
system_1.make_a_booking(booking_4)

print("All the customer = " , system_1._customers)
print("All the bookings = " , system_1._bookings)
print("All the cars = ", system_1._cars)
print("All the unpaid = ", system_1._payment)

print("now let customer 2 (C002) pay")
system_1.confirmation(customer_2,car_1,booking_1)
system_1.accept_payment(customer_2.get_customer())

print("All the customer = " , system_1._customers)
print("All the bookings = " , system_1._bookings)
print("All the cars = ", system_1._cars)
print("All the unpaid = ", system_1._payment)

print("customer_2 (C002) has succesfully paid the booking")
