a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))

d = []

def sumofnumbers(a,b,c,d):
    for i in range(a,b+1):
        if i%c == 0:
            d.append(i)
    return(sum(d))

sum = sumofnumbers(a,b,c,d)
print(sum)

        
        