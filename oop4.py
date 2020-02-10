# Python Object-Oriented Programming

# Inheritance- CreatingSubClases
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

# descendant of Employee
class Developer(Employee):
    raise_amount=1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        #Employee.__init__(self,first,last,pay)

# descendant of Employee
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees= employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev1 = Developer('Corey','Schafer',50000,'Python')
dev2 = Developer('Fatih','Fikri',60000,'Java')

mgr_1 = Manager('Sue','Smith',90000,[dev1]) 

print(isinstance(mgr_1,Employee))

print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))


"""
mgr_1.add_emp(dev2)
mgr_1.remove_emp(dev1)
mgr_1.print_emps() """





#print(help(Developer))
#print(dev1.email)
#print(dev2.email)

"""print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)"""

""" print(dev1.email)
print(dev1.prog_lang) """
