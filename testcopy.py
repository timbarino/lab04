from car import *
from admin import *
from admin_system import *
from customer import *
from booking import *
from insurance import*
from location import*
from rental_system import *
#self,name,ID,user_name,pass_word
print("\n")
admin_1 = Admin("kirito","A001","kirito","666666" )
print("Admin user name:",admin_1.get_user_name)
print("Admin password", admin_1.get_pass_word)
#add admin_1 to admin_system
AdminSystem = Admin_system
AdminSystem.add_admin(Admin("kirito","A001","kirito","666666" ))
print("password check:", AdminSystem.check_user_name("kirito","666666"))
print("\n")

print("the first customer")
customer_1 = Customer("C001","tim","L123456","tim@gmail.com")
print("customer id: ", customer_1.get_customer())
print("customer name: ", customer_1.get_name())
print("customer licence: ", customer_1.get_licence())
print("customer email: ", customer_1.get_email())
print("\n")


location_1 = Location("darling harbour", "maroubra")
print("pick up location", location_1.get_pick_up)
print("drop off location", location_q.get_drop_off)

print("the second customer")
customer_2 = Customer("C002","customer 2", "L222222","c2@gmail.com")
print("customer id: ", customer_2.get_customer())
print("customer name: ", customer_2.get_name())
print("customer licence: ", customer_2.get_licence())
print("customer email: ", customer_2.get_email())
print("\n")

location_2 = location("the start location", "the end location")
print("Pick up location:", location_2.get_pick_up())
print("Drop off location:", location_2.get_drop_off())
print("\n")


car_1 = small_car("reg1","model1","carid1")
car_2 = medium_car("reg1","model1","carid1")
car_3 = large_car("reg1","model1","carid1")
car_4 = premium_car("reg1","model1","carid1")

system_1 = rental_system()
booking_1 = booking(1,car_1,cuomer_1,"location 1",1)
booking_1 = booking(2,car_2,cuomer_1,"location 2",2)
booking_1 = booking(3,car_3,cuomer_1,"location 3",3)
booking_1 = booking(4,car_4,cuomer_1,"location 4",4)

print("All the customer = ", system_1.customers)
print("all the booking", systme_1.bookings)
print("all the cars =", system_1.cars)
print("all the unpaid ", system_1.payment)

############
print("now let customer 2 (C002) pay")

system_1.accept_payment(customer_2.get_customer())

print("All the customer = " , system_1._customers)
print("All the bookings = " , system_1._bookings)
print("All the cars = ", system_1._cars)
print("All the unpaid = ", system_1._payment)

print("customer_2 (C002) has succesfully paid the booking")
##############
print("now let customer 2(C002) pay")
system_1_accept_payment(customer_2.get_customer())
rint("All the customer = ", system_1.customers)
print("all the booking", systme_1.bookings)
print("all the cars =", system_1.cars)
print("all the unpaid ", system_1.payment)

print("customer_2 (C002) has succesfully paid the booking")
