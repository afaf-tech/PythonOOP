# Python Object-Oriented Programming

# Special ( Magic / Dunder ) Methods
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

    # print our string object 
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Fatih','Fikri',60000)


#
#print(len('test'))
#print('test'.__len__())

#print(emp1 + emp2) #printed due to there is add method on Employee obj
 

""" print(emp1)
print(repr(emp1))
print(str(emp1)) """

#these mthods change how method to be displayed
#print(emp1.__repr__())
#print(emp1.__str__())



# give the same result
#print(1+2)
#print(int.__add__(1,2))
#print(str.__add__('a','b')) # concat those together
