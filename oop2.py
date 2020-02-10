# Python Object-Oriented Programming

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    #it's like a consructor on other languages
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount)

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Fatih','Fikri',50000)

#both might be the same
#print(Employee.fullname(emp1))
#print(emp2.fullname())
#emp1.raise_amount=1.05
print(Employee.num_of_emps)

#print(emp1.__dict__)
#print(Employee.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)