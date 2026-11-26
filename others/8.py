class Staff:
    def __init__(self,amount):
        self.amount=amount
    def monthly_pay(self):
        return self.amount
class Lecturer(Staff):
    def __init__(self, amount,allowance):
        super().__init__(amount)
        self.allowance= allowance
    def monthly_pay(self):
        return super().monthly_pay() + self.allowance
class NonTeachingStaff(Staff):
    def __init__(self, amount,rate,hours):
        super().__init__(amount)
        self.hours=hours
        self.rate=rate
    def monthly_pay(self):
        return super().monthly_pay() + (self.hours * self.rate)
class ContractStaff(Staff):
    def __init__(self, amount,days,rate):
        super().__init__(amount)
        self.days= days
        self.rate =rate
    def monthly_pay(self):
        return self.days * self.rate
staffs = [Lecturer(30000,200),NonTeachingStaff(30000,0.6,3),ContractStaff(30000,5,0.8)]
for s in staffs:                                                                                                                                                                        
    print(s.monthly_pay())