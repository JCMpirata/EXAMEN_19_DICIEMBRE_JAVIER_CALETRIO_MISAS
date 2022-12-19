class lunes:
    def __init__(self, año):
        self.año = año

    def edad(self):
        nacimiento = int(input("Ingrese su año de nacimiento: "))
        return self.año - nacimiento

        