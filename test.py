inputstr = 'hello'
shift = 0
result = ''
inputstr.lower()
for i in range(len(inputstr)):
    char = inputstr[i]
    print(char)
    result += chr((ord(char) + shift-97) % 26 + 97)
    print(chr((ord(char) + shift-97) % 26 + 97))
print(result)