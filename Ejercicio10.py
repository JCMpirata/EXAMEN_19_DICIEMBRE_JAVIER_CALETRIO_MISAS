def xbonacci(num: int):
    lista = [0, 1, 2]
    for i in range(num):
        lista.append(lista[-1] + lista[-2] + lista[-3])
        return lista[-1]

if __name__ == '__main__':
    n = int(input("Ingrese un número: "))
    print(xbonacci(n))
    