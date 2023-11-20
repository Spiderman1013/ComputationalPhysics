import math

def quadEquation(a, b, c):
    det = math.sqrt(b**2 - 4*a*c)
    print("x1 = ", (-b + det)/(2*a))
    print("x2 = ", (-b - det)/(2*a))

def quadEquation2(a, b, c):
    det = math.sqrt(b**2 - 4*a*c)
    print("x1 = ", 2*c/(-b + det))
    print("x2 = ", 2*c/(-b - det))

def improvedQuadEquation(a, b, c):
    det = math.sqrt(b**2 - 4*a*c)
    if abs(b + det) > abs(b - det):
        x1 = (-2*c) / (b + det)
        x2 = (b + det) / (2*a)
    else:
        x1 = (-b + det) / (2*a)
        x2 = (-2*c) / (b - det)
    print("x1 = ", x1)
    print("x2 = ", x2)

def main():
    quadEquation(0.001, 1000, 0.001)
    quadEquation2(0.001, 1000, 0.001)
    improvedQuadEquation(0.001, 1000, 0.001)

if __name__ == "__main__":
    main()