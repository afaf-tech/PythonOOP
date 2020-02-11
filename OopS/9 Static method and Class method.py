class Hero:
    # private class variable
    __jumlah = 0

    # jika ada arg self maka method =
    # hanya berlaku untuk object bukan kelas jadi tidak bisa mengkakses class variable
    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1  # menambah jumlah +1 setiap kali class Hero di instansiasi

    # method ini tidak berlaku untuk object tapi beralku untuk class
    def getJumlah():
        return Hero.__jumlah

    # method static (decorator) nempel ke object dan kelasnya
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # cuma nempel ke kelas jika ada arg cls
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


snipper = Hero('snipper')
print(snipper.getJumlah2())
rikimaru = Hero('rikimaru')
print(snipper.getJumlah2())
drowranger = Hero('drownranger')
print(Hero.getJumlah3())
