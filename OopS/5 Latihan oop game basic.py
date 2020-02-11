class Hero:

    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)  # self yang menyerang5

    def diserang(self, lawan, attackPowerLawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPowerLawan / self.armorNumber
        print('serangan terasa adalah : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

snipper = Hero('snipper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

# object dikirim melalui arg
snipper.serang(rikimaru)
print("\n")
rikimaru.serang(snipper)
rikimaru.serang(snipper)
rikimaru.serang(snipper)
rikimaru.serang(snipper)
rikimaru.serang(snipper)
