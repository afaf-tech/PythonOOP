# Python Object-Oriented Programming

class Employee:
    #it's like a consructor on other languages
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Fatih','Fikri',50000)

#both might be the same
#print(Employee.fullname(emp1))
#print(emp2.fullname())