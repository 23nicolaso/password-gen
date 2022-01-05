import random

symbolCount = int(input("How many symbols? "))
numberCount = int(input("How many numbers? "))
letterCount = int(input("How many letters? "))
length = symbolCount + numberCount + letterCount

possibleLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ""
symbols = 0
numbers = 0
letters = 0

for i in range(length):
    randomChoice = random.randint(0, 2)
    if randomChoice == 0:
        if symbols < symbolCount:
            # Insert random symbol into password string
            password += chr(random.randint(33, 47))
            symbols += 1
        elif numbers < numberCount:
            # Insert random number into password string
            password += str(random.randint(0, 9))
            numbers += 1
        else:
            # Insert random letter into password string
            password += possibleLetters[random.randint(0, 52)]
            letters += 1

    if randomChoice == 1:
        if numbers < numberCount:
            # Insert random number into password string
            password += str(random.randint(0, 9))
            numbers += 1
        elif symbols < symbolCount:
            # Insert random symbol into password string
            password += chr(random.randint(33, 47))
            symbols += 1
        else:
            # Insert random letter into password string
            password += possibleLetters[random.randint(0, 52)]
            letters += 1
    if randomChoice == 2:
        if letters < letterCount:
            # Insert random letter into password string
            password += possibleLetters[random.randint(0, 52)]
            letters += 1
        elif symbols < symbolCount:
            # Insert random symbol into password string
            password += chr(random.randint(33, 47))
            symbols += 1
        else:
            # Insert random number into password string
            password += str(random.randint(0, 9))
            numbers += 1

print(password)
