# Python Object-Oriented Programming

# Property Decorator - Getter, Setter, And Deleters
class Employee:
    __secretAttr=10
    #it's like a consructor on other languages
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property # to make method behave like a property so we can call it without ()
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first= None
        self.last= None

  

emp1 = Employee('John','Smith')

emp1.fullname ='Cobey Schreaver'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
print(emp1.__secretAttr)


del emp1.fullname

print(emp1.fullname)

