class Vehicle:                                                       #base class
    def __init__(self,model,rental_rate):
        self.model=model
        self.rental_rate=rental_rate

    def calculate_rental(self,days):
        return self.rental_rate*days

class car(Vehicle):                                                    #Subclass
    def __init__(self,model,rental_rate,seats):
        super().__init__(model,rental_rate)
        self.seats=seats

    def calculate_rental(self,days):
        return (self.rental_rate*days) + 500

class Bike(Vehicle):                                                    #Subclass
    def __init__(self,model,rental_rate,helmet_charge):
        super().__init__(model,rental_rate)
        self.helmet_charge=helmet_charge

    def calculate_rental(self,days):
        return (self.rental_rate*days) + self.helmet_charge

class Truck(Vehicle):                                                    #Subclass
    def __init__(self,model,rental_rate,load_charge):
        super().__init__(model,rental_rate)
        self.load_charge=load_charge

    def calculate_rental(self,days):
        return (self.rental_rate*days) + self.load_charge



c = car("Swift",2500,5)

b = Bike("Honda",1500,250)

t = Truck("TATA",3500,500)

print(c.calculate_rental(5))
print(b.calculate_rental(5))
print(t.calculate_rental(5))