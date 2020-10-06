import re

password = input("password! ")

lowercase = bool(re.findall("[a-z]", password))
uppercase = bool(re.findall("[A-Z]", password))
number = bool(re.findall("[0-9]", password))
special = bool(re.findall("[!@#$%^&*()]", password))

length = len(password)
print(length)


if number:
    if lowercase and uppercase:
        if special:
            if length < 6:
                print("level 0")
            elif length < 9:
                print("level 1")
            elif length < 11:
                print("level 2")
            elif length < 13:
                print("level 3")
            else:
                print("level 4")
        else:
            if length < 6:
                print("level 0")
            elif length < 9:
                print("level 1")
            elif length < 11:
                print("level 2")
            elif length < 14:
                print("level 3")
            else:
                print("level 4")
    else:
        if length < 11:
            print("level 0")
        elif length < 16:
            print("level 1")
        else:
            print("level 2")
elif lowercase:
    if uppercase:
        if length < 7:
            print("level 0")
        elif length < 10:
            print("level 1")
        elif length < 12:
            print("level 2")
        elif length < 15:
            print("level 3")
        else:
            print("level 4")
    else:
        if length < 8:
            print("level 0")
        elif length < 11:
            print("level 1")
        elif length < 14:
            print("level 2")
        elif length < 18:
            print("level 3")
        else:
            print("level 4")
elif uppercase:
        if length < 8:
            print("level 0")
        elif length < 11:
            print("level 1")
        elif length < 14:
            print("level 2")
        elif length < 18:
            print("level 3")
        else:
            print("level 4")
else:
    print("there are no numbers or letters, please give a password with at least on of the two")
