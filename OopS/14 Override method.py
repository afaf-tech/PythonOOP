class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("show info di class Hero")
        print("{] health : {} ".format(self.name, self.health))

class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    #method override
    def showInfo(self):
        print("show info di subclass Hero Intelligent")
        print("{} \n\tTipe : intelligent, \n\t: {}".format(
            self.name,
            self.health
        ))

class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name,200)


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo()