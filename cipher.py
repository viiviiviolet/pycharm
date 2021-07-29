# importing randomness and list manipulation
import random
import itertools
import time

# initialize variables
method = ''
keystring = []
shift = 0
shiftword = ''


# caesar cipher function
def caesar(inputstr, shift):
    result = ''
    inputstr.lower()
    for i in range(len(inputstr)):
        char = inputstr[i]
        result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


# vigenere cipher function
def vigenere(inputstr, keyword):
    result = ""
    keywordlist = []
    inputstr.lower()
    keyword.lower()
    # loop to convert keyword to string of shifts
    for x in range(len(keyword)):
        char = inputstr[x]
        charnum = ord(char) - 97
        charnum %= 26
        keywordlist.append(charnum)
    list(itertools.islice(itertools.cycle(keywordlist), len(inputstr)))
    for i in range(len(inputstr)):
        char = inputstr[i]
        result += chr((ord(char) + keywordlist[i] - 97) % 26 + 97)
    return result


# one time pad function
def onetimepad(inputstr):
    result = ''
    rnum = 0
    inputstr.lower()
    for y in range(len(inputstr)):
        char = inputstr[y]
        rnum = random.randint(0, 26)
        result += chr((ord(char) + rnum - 97) % 26 + 97)
        keystring.append(rnum)
    return result


# main function
while True:
    keyphrase = input('What would you like to encode? (please only input letters, the program is not case sensitive ')
    while True:
        encodingmethod = int(input(
            'What method would you like to use?\n1. Caesar Cipher\n2. Vigenere Cipher\n3. One Time Pad\n'))
        if encodingmethod == 1:
            shift = int(input("Please input a shift number between 0 and 25"))
            output = caesar(keyphrase, shift)
            method = "the caesar cipher"
            break
        elif encodingmethod == 2:
            shiftword = input('Please input a password to encode with')
            output = vigenere(keyphrase, shiftword)
            method = "the vigenere cipher"
            break
        elif encodingmethod == 3:
            output = onetimepad(keyphrase)
            method = "a one time pad"
            break
        else:
            print("Please input a valid number")
    print(f"{keyphrase} encoded using {method} is {output} ")
    if encodingmethod == 1:
        print(f'The shift used for the caesar cipher is {shift}')
    elif encodingmethod == 2:
        print(f'The password used for the cipher is {shiftword}')
    elif encodingmethod == 3:
        print(f'The one time pad numbers generated are {keystring}')
    while True:
        repeat = input("Would you like to repeat the program? (y/n)")
        if repeat == 'y':
            break
        elif repeat == 'n':
            print('Goodbye!')
            time.sleep(5.0)
            quit()
        else:
            print("Please enter a valid input.")
