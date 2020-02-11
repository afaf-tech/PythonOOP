class Hero:

    def __init__(self,name, health):
        self.name = name
        self.health = health

class Hero_iintelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

lina = Hero('lina', 100)
techies = Hero_iintelligent('techies', 50)
axe= Hero_strength('axe', 200)

print(lina.name)
print(techies.name)
print(axe.name)
