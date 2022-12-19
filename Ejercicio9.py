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
            lunes = 0
        return lunes



if __name__ == '__main__':
    lunes = lunes(año = datetime.datetime.now().year)
    print(lunes.edad(nacimiento = int(input("Ingrese su año de nacimiento: "))))
    print(lunes.trabajar())


        