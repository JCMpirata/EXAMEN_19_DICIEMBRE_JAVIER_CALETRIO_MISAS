class lunes:
    def __init__(self, año):
        self.año = año

    def edad(self):
        nacimiento = int(input("Ingrese su año de nacimiento: "))
        return self.año - nacimiento

    def trabajar(self):
        if self.edad() >= 22 and self.edad() <= 78:
            print("Puede trabajar")
        else:
            print("No puede trabajar")