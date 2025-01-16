from datetime import date, timedelta

class Member:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.expiry_date = date.today() + timedelta(days=365)  

    def __str__(self):
        return f"{self.__class__.__name__}: {self.first_name} {self.last_name}, Expiry Date: {self.expiry_date}"

class Admin(Member):
    def __init__(self, first_name, last_name, secret_code):
        super().__init__(first_name, last_name) 
        self.secret_code = secret_code
        self.expiry_date = date.today() + timedelta(days=36500) 

    def __str__(self):
        return super().__str__() + f", Secret Code: {self.secret_code}"

# Create an Admin object
admin = Admin("John", "Doe", "1234")
print(admin)  # Output Admin details

# Create a regular Member object
user = Member("Jane", "Smith")
print(user)  # Output Member details
