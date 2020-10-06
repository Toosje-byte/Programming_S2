import string
import random

x= 0

while x < 1:
    N = int(input("how many numbers? "))
    U = int(input("how many uppercase letters? "))
    L = int(input("how many lowercase letters? "))
    S = int(input("how many symbols? "))
    Length = int(input("how long? "))
    y = N + U + L + S
    if y <= Length:
        x = 1
    else:
        print("password is too short try again")

dif = Length - y

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = '0123456789'
symbols = '!@#$%^&*()'
all = uppercase + lowercase + numbers + symbols

password = ''.join((random.choice(uppercase) for i in range(U)))
password += ''.join((random.choice(lowercase) for i in range(L)))
password += ''.join((random.choice(numbers) for i in range(N)))
password += ''.join((random.choice(symbols) for i in range(S)))
password += ''.join((random.choice(all) for i in range(dif)))

# Python code to convert string to list character-wise
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

passlist = Convert(password)
random.shuffle(passlist)
password = ''.join(passlist)

print("your password is: " + password)
