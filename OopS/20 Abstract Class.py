# membuat class abstract
# abc  = abstract base class   karena di python  tidak ada keyword abstract

from abc import ABC, abstractmethod

# konsep intinya adalah seperti surat kontrak
# abstract class button adalah blueprint untuk kelas2 yang mengimplementasi button
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print("push button click")

class RadioButton(Button):
    def click(self):
        print("Radio butten clicked")

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
help(tombol1)