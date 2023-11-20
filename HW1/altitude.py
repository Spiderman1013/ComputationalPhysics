import math

GRAVITY = 6.67e-11
EARTH_MASS = 5.97e24
EARTH_RADIUS = 6.371e3

def altitude(T):
    T= T*60*60 #converts T to seconds from hours
    h = ((GRAVITY*EARTH_MASS*T**2)/(4*math.pi**2))**(1/3) - EARTH_RADIUS
    return h

def main():
    T = input("Enter the period of the satellite in hours: ")
    print("The altitude of the satellite is", "{:e}".format(altitude(float(T))), "meters.")

if __name__ == "__main__":
    main()