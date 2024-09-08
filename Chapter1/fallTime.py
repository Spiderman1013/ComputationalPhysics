import math

def timeFall(height):
    g = 9.8
    return math.sqrt((2 * height * g))

def main():
    height = float(input("Enter the height of the tower in meters: "))
    print("The time it takes the ball to fall", height, "meters is", round(timeFall(height),2), "seconds.")

if __name__ == "__main__":
    main()