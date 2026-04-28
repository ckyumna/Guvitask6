class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class RegualarEmployee(Employee):
    def __init__(self,name,salary,bonous):
        super().__init__(name,salary)
        self.bonus = bonous

    def calculate_salary(self):
        return self.salary+self.bonus

class ContratEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name,0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked

class Manager(Employee):
    def __init__(self,name,salary,allowance):
        super().__init__(name,salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.allowance+self.salary


r=RegualarEmployee("yumna",10000,5000)
c=ContratEmployee("alice",1000,42)
m=Manager(name="Bob",salary=10000,allowance=5000)

print("name : ",r.name,"salary : ",r.calculate_salary())
print("name : ",c.name,"salary : ",c.calculate_salary())
print("name : ",m.name,"salary : ",m.calculate_salary())