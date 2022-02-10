import math
a = int (input("enter any number: "))
f = 1
def factorial_num(a,f):
    for i in range(1,a+1):
        f = f*i
    print(f)
    
factorial_num(a,f)