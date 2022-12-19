def Tribonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3)

if __name__ == '__main__':
    n = int(input("Introduce un numero: ").strip())
    print(Tribonacci(n))