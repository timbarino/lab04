from car import *
from admin import *

class Admin_system():
      def __init__(self):
         self.Admin_list = []
         self.Car_list = []

      def add_car(self,car):
         self.Car_list.append(Car)

      def add_admin(self,Admin):
         self.Admin_list.append(Admin)

      def check_user_name(self,user_name,pass_word):
         for account in self.Admin_list:
            if (account.get_user_name() == user_name) and (account.get_pass_word() is pass_word):
                  return 1
         return 0     
