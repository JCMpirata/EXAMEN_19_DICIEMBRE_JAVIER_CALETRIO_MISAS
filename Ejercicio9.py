import datetime


def lunes(cumpleaños, today):
    diferencia = today - cumpleaños
    lunes = diferencia.days // 7
    return lunes

if __name__ == '__main__':
    cumpleaños = datetime.datetime.strptime(input("Ingrese su fecha de cumpleaños: "), "%d-%m-%Y")
    today = datetime.datetime.strptime(input("Ingrese la fecha de hoy: "), "%d-%m-%Y")
    print(lunes(cumpleaños, today))



        