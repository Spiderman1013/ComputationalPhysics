def bindingEnergy(Z, A):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2

    if (Z%2==0 and (A-Z)%2==0):
        a5 = 12.0
    elif (Z%2==1 and (A-Z)%2==1):
        a5 = -12.0
    else:
        a5 = 0.0

    return (a1 * A) - (a2 * A ** (2 / 3)) - (a3 * (Z ** 2) / (A ** (1 / 3))) - (a4 * (A - 2 * Z) ** 2 / A) + (a5 / A ** (1 / 2))

def bindingEnergyPerNucleon(Z, A): 
    return bindingEnergy(Z, A) / A

def mostStableAtomicNumber(Z):
    ZNew = int(Z)
    maxA = ZNew
    for A in range(ZNew, 3*ZNew):
        if bindingEnergyPerNucleon(ZNew, A) > bindingEnergyPerNucleon(ZNew, maxA):
            maxA = A
    return maxA

def main():
    for Z in range(1, 101):
        print("Z =", Z, "A =", mostStableAtomicNumber(Z), "BE/A =", bindingEnergyPerNucleon(Z, mostStableAtomicNumber(Z)))
        
if __name__ == "__main__":
    main()