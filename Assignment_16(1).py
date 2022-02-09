stutters = input("Enter Any String:")
stutter = stutters.split()

def Stutter(stutter):
    for i in stutter:
        print(f"{i[0]}{i[1]}...{i[0]}{i[1]}... {stutters}?")

Stutter(stutter)
            
    