a = input("Enter any String Contains Vowels: ")
b = ['a','e','i','o','u']
def replace_vowels(a,b):
    for i in a:
        for j in b:
            if i == j:
                a = a.replace(i,"#")
                print(a)



rw = replace_vowels(a,b)

