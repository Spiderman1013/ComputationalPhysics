def catalan_number(n):
    if n == 0:
        return 1
    else:
        return (((4 * n) - 2) / (n + 1)) * catalan_number(n - 1)
    
def main():
    print("Here are all Catalan numbers less than 1 billion")
    m = 0
    number = catalan_number(m)
    while(number < 1e9):
        print(number)
        m = m + 1
        number = catalan_number(m)

if __name__ == "__main__":
    main()