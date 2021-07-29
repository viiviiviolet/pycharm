# initializing variables
number = 0
conversionfrom = ''
conversionto = ''
output = 0
numberCheck = False


# function to check if integer is binary
def checkbinary(inputint):
    binaryset = {'0', '1'}
    inputset = set(str(inputint))
    if binaryset == inputset or inputset == {'0'} or inputset == {'1'}:
        return True
    else:
        return False


# function for converting decimal to binary
def convertbinary(decimal):
    finished = False
    counter = 0
    final = 0
    while not finished:
        remainder = decimal % 2
        final += (remainder * (10 ** counter))
        decimal //= 2
        counter += 1
        if decimal == 0:
            finished = True
    return final


# function for converting binary to decimal
def convertdecimal(binary):
    final = 0
    numlist = [int(x) for x in str(binary)]
    numlist.reverse()
    for i in numlist:
        final += (i * (2 ** numlist.index(i)))
    return final


# Loop for error checking
while not numberCheck:
    number = int(input("Enter an integer:"))
    base = int(input("Is the integer\n1. Binary\n2. Decimal\n"))
    if base == 1:
        numberCheck = checkbinary(number)
        output = convertdecimal(number)
        conversionfrom = 'binary'
        conversionto = "decimal"
    elif base == 2:
        numberCheck = True
        output = convertbinary(number)
        conversionfrom = 'decimal'
        conversionto = 'binary'
    else:
        print('Invalid Input')

# formatted string for output
print(f'The integer {number} converted from {conversionfrom} to {conversionto} is {output}.')
