import math
import os
import random
import re
import sys

def hollow_triangle(altura):
    for i in range(1, altura + 1):
        print(("_" * (altura - i)) + "#" * i + "_" * (altura - i))

if __name__ == '__main__':
    altura = int(input("Introduce un numero: ").strip())
    hollow_triangle(altura)
