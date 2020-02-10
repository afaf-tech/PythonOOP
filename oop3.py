# Python Object-Oriented Programming

# Regular method automatically passes the instance as the first argument(self)
# Class method automatically passes Class as the first argument(cls)
# static method doesnt pass anything when created
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_string):
        first , last, pay = emp_string.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Fatih','Fikri',50000)


import datetime
my_date = datetime.date(2016, 7,11)
print(Employee.is_workday(my_date))
#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Steve-Smith-30000'
#emp_str_3 = 'Jane-Doe-90000'


#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#rint(new_emp_1.pay)



#Employee.set_raise_amt(1.05) # equals to Employee.raise_amt = 1.05

#regular method, class method and static method

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)