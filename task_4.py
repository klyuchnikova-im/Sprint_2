class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        
    @classmethod    
    def get_hours(cls, name, hours, rest_days, email):
        if hours == '' or hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email) 
    @classmethod    
    def get_email(cls, name, hours, rest_days, email):        
        if email == '' or email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod                
    def set_hourly_payment(cls, change_hourly_payment):
        cls.hourly_payment = change_hourly_payment

    def salary(self):
        total_salary = self.hours * self.hourly_payment
        return total_salary