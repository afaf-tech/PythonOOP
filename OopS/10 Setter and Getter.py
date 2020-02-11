class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    # membuat method as if property jadi ketika memanggil tidak usah menggunakan()
    @property
    def info(self):
        return "name : {}  \n health: {}".format(self.name, self.__health)

    # def getHealth(self):
    #     return self.__health
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor deleted')
        self.__armor = None


sniper = Hero('sniper', 100, 10)
print("merubah info")
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

print('getter and setter untuk armor :')

print(sniper.armor)
sniper.armor = 50
print(sniper.__dict__)

print('delete armor sniper')
del sniper.armor
print(sniper.__dict__)