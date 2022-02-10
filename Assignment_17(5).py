string1 = input("Enter String 1: ")
string2 = input("Enter String 2: ")
count = 0
i = 0
def hamming(string1,string2,count,i):
    while(i<len(string1)):
        if string1[i] != string2[i]:
            count = count+1
        i = i+1
    print(count)
    
hamming(string1,string2,count,i)
