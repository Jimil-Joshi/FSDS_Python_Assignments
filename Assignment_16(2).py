import math

n = int(input("Enter Radians to convert into the degree: "))

def convert(n):
    angle  = math.degrees(n)
    angle = "{:.1f}".format(angle)
    print(f"Radians to Degree: {angle}")
    
convert(n)
    