import math
import numpy as np


def main():
    L = 100
    M = 0
    for x in range(-L, L+1):
        for y in range(-L, L+1):
            for z in range(-L, L+1):
                if x == y == z == 0:
                    continue
                r = ((x**2 + y**2 + z**2) ** -0.5)
                if ((x + y + z)%2 == 0):
                    M = M+r
                else:
                    M = M-r
    print(M)

if __name__ == "__main__":
    main()