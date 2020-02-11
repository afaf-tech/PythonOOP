# aturan enkapsulasi
# 1. buat semua variable private
# 2. adanya getter setter 


class Hero:

    def __init__(self, name, health, attackPower):
        # semua variable di bawah is private jadi hanya bisa diakses oleh anggota kelas sendiri
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealt(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attackPower = nilaiBaru

# game berjalan
earthShaker = Hero("earthShaker", 50, 5)

print(earthShaker.__dict__)
print(earthShaker.getName())
print(earthShaker.getHealt())
earthShaker.diserang(5)
print(earthShaker.getHealt())
earthShaker.setAttPower(10)
print(earthShaker.__dict__)
