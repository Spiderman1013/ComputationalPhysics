def simpsonsIntegrator(func, a, b, n ):
    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n, 2):
        result += 4 * func(a + i * h)

    for i in range(2, n-1, 2):
        result += 2 * func(a + i * h)

    result *= h / 3
    return result


def main():
    a = 0
    b = 2
    n = 1000
    print(simpsonsIntegrator(lambda x: (x**4 - 2*x + 1), a, b, n))

if __name__ == "__main__":
    main()