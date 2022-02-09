import math

s = int(input("Enter Any Number: " ))
def ah(s):
    a = ((3*math.sqrt(3))*(s**2))/2
    a = "{:.1f}".format(a)
    print(a)
ah(s)