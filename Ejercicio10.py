def Xbonacci(n):
    lista = [0, 1]
    for i in range(n):
        lista.append(lista[-1] + lista[-2])
    return lista[-1]

if __name__ == '__main__':
    n = int(input("Ingrese un número: "))
    print(Xbonacci(n))

    