import random


def password_generator(length):

    allCharacters = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r",
                     "t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z",
                     "x","c","v","b","n","m",",",".","/"]
    password = ''
    for i in range(length):
        random_num = random.randrange(0,len(allCharacters))
        newChar = allCharacters[random_num]
        password += newChar
    return password




