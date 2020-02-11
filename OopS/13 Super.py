class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health : {}".format(self.name, self.health))

class Hero_iintelligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        # we take init on Hero without giving self
        super().__init__(name, 100)
        super().showInfo()


class Hero_strength(Hero):
    def __init__(self, name):
        # self.name = name
        # self.health = 200
        Hero.__init__(self, name, 200)
        super().showInfo()



lina = Hero_iintelligent('lina')
axe = Hero_strength('axe')

print(lina.name, " ", lina.health)
print(axe.name, " ", axe.health)
