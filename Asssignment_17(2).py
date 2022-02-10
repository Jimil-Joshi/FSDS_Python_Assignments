n = input("Enter Any range for check in equality: ")

def check(n):
    evaluation = eval(n)
    if evaluation:
        return True
    else:
        return False
    
print(check(n))