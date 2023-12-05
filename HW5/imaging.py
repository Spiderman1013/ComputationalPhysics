import math
import random

def generate_random_string():
    """Generates a random bitstring of 14 characters"""
    return ''.join(random.choice('01') for _ in range(14))

def count_occurance(string):
    """Counts the number of occurances of '101' in a bitstring"""
    count = 0
    for i in range(len(string)-3):
        if string[i:i+3] == '101':
            count += 1
    return count 


def main():
    N = 1e6 
    EV = 0

    for i in range(int(N)):
        bitstring = generate_random_string()
        ev = count_occurance(bitstring)
        print(ev)
        EV += ev
        if i == 0:
            continue #avoid divide by zero
        else:
            print(EV/i)

if __name__ == "__main__":
    main()