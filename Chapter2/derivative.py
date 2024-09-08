def derivative(f, x, e):
    return (f(x + e) - f(x)) / e

def main():
    e = 10e-2
    value = 1 
    while(e > 10e-16):
        print("The derivative of x(x-1) with epsilon=",e,"is",derivative(lambda x: x*(x-1), value, e))
        e = e*(10e-2)

if __name__ == "__main__":
    main()