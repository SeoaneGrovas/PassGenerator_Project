# Random pass generator v.1.0
import random
import string

def password(length,num=False,strenght="weak"):
    # Length of password, num if you want a number, and strenght
    # (weak, strong, very_strong).
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ""
    if strenght == "weak":
        if num:
            length -=2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)
            
    elif strenght == "strong":
        if num:
            length -=2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)
    elif strenght == "very_strong":
        ran = random.randint(2,4)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)

    pwd = list(pwd)
    random.shuffle(pwd)
    return "".join(pwd)

# This print is to test this code.
print(password(15,num=True,strenght="very_strong"))