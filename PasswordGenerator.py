"""
    Goal : Make a strong Password Generator
"""
import random
symbols = ['!','@','#','$','£','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',';',':',',','.','<','>','/','?']
numbers = list()
for i in range(48,58):
    numbers.append(chr(i))
alphabets = list()
for i in range(97,123):
    alphabets.append(chr(i))
Alphabets = list()
for i in range(65,91):
    Alphabets.append(chr(i))
charset = [symbols , numbers , alphabets , Alphabets]

while True:
    print("==============================================================")
    print("                WELCOME TO PASSWORD GENERATOR                 ")
    print("==============================================================")
    while True:
        length = int(input("Enter Desired Length of the Password : "))
        if length >= 10 :
            break
        else:
            print("\nLength should not be less than 10.")
            print("Please Try Again!!!\n")
            continue
    password = ""
    password += random.choice(symbols)
    length -= 1
    while length > 0 :
        x = random.choice(charset)
        password += random.choice(x)
        length -= 1
    print("Suggested Password :",password)
    print("==============================================================")
    choice = input("\nDo you wanna try again? ").lower()
    if choice == "yes" or choice == "y":
        continue
    else:
        break
