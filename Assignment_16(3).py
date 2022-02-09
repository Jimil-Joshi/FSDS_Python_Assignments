n = int(input("Enter Any Number: "))

def curzon(n):
    c = pow(2,n)+1
    d = 2*n+1
    if c%d == 0:
        print(f"{n} is curzon number")
    else:
        print(f"{n} is not a curzon number")
curzon(n)