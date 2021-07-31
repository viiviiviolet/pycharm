finished = False
integer = None
while True:
    while True:
        integerstring = input("Please enter a positive integer. ")
        if integerstring.isdigit():
            integer = int(integerstring)
            if integer <= 0:
                print("Please enter a valid positive integer")
            else:
                break
        else:
            print("Please enter a valid positive integer")
    while not finished:
        print(integer)
        if integer % 2 == 1:
            integer = (integer * 3) + 1
        elif integer % 2 == 0:
            integer //= 2
        if integer == 1:
            print(1)
            finished = True
    print("Finished")
    while True:
        again = input("Would you like to run the program again? (y/n)")
        again.lower()
        if again == "y":
            break
        elif again == 'n':
            quit()
        else:
            print("Please enter a valid input")

