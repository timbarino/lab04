class Customer():
    def __init__(self,customer_ID, name, license, email,age):
        self.customer_ID = customer_ID
        self.name = name
        self.license = license
        self.email = email
        self.age = age
    def get_customer(self):
        return self.customer_ID
    def get_name(self):
        return self.name
    def get_license(self):
        return self.license
    def get_email(self):
        return self.email
    def get_age(self):
        return self.age
