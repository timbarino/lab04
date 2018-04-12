#remember to implement as Abstract Class
from abc import ABC, abstractmethod

class Car(ABC):
	def __init__(self,registration,model,car_ID,status):	#model == type
		self._car_id = car_ID
		self._registration = registration
		self._model = model
		self._status = status
	@abstractmethod
	def __str__(self):
		pass
	

class small_car(Car):
	def __init__(self,registration,model,car_ID,status):
		self._daily_fee = 1
		super().__init__(registration,model,car_ID,status)
	
	def __str__(self):
		return "small car ,registration %s ,model %s,car_ID %d,status %s, daily_fee %d" %(self.__registration, self._model, self._car_id, self._status,self._daily_fee)
	
		
class medium_car(Car):
	def __init__(self,registration,model,car_ID,status):
		self._daily_fee = 2
		super().__init__(registration,model,car_ID,status)
	
	def __str__(self):
		return "medium car ,registration %s ,model %s,car_ID %d,status %s, daily_fee %d" %(self.__registration, self._model, self._car_id, self._status,self._daily_fee)
	
class large_car(Car):
	def __init__(self,registration,model,car_ID,status):
		self._daily_fee = 3
		super().__init__(registration,model,car_ID,status)
	
	def __str__(self):
		return "large car ,registration %s ,model %s,car_ID %d,status %s, daily_fee %d" %(self.__registration, self._model, self._car_id, self._status,self._daily_fee)
	
class premium_car(Car):
	def __init__(self,registration,model,car_ID,status):
		self._daily_fee = 4
		super().__init__(registration,model,car_ID,status)
	
	def __str__(self):
		return "premium car ,registration %s ,model %s,car_ID %d,status %s, daily_fee %d" %(self.__registration, self._model, self._car_id, self._status,self._daily_fee)
	


