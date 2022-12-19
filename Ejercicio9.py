import datetime

class lunes:
    def __init__(self, año):
        self.año = año

    def edad(self, nacimiento):
        self.nacimiento = int(input("Ingrese su año de nacimiento: "))
        return self.año - self.nacimiento

    def trabajar(self):
        if self.edad() >= 22 and self.edad() <= 78:
            print("Puede trabajar")
            lunes = (self.año - self.nacimiento)/7
        else:
            print("No puede trabajar")

    