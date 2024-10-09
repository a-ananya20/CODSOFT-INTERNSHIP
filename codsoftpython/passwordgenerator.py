import random
import string
def passwordgen():
    passLength=int(input("Enter password length: "))
    letters= string.ascii_letters
    randomChoice = random.choices(letters,k=passLength)
    randomString= ''.join(randomChoice)
    print(randomString)
passwordgen()
    