import math

def nonRelativisticTime(d, v):
    return d / v

def relativisticTime(d, v):
    g = 1/(math.sqrt(1 - v**2))
    return nonRelativisticTime(d, v) * g

def main():
    d = float(input("Enter the distance in light-years: "))
    v = float(input("Enter the speed as a fraction of c: "))
    print("The non-relativistic time is", round(nonRelativisticTime(d, v),2), "years.")
    print("The relativistic time is", round(relativisticTime(d, v),2), "years.")

if __name__ == "__main__":
    main()