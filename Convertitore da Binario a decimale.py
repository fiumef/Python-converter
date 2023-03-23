def data_type():
    """data_type takes no argument and asks the user if he wants to convert a binary or a decimal into the other form
    then calls the appropriate function based on the input"""
    while True:
        x = input('Do you want to convert a Binary or Decimal?\n press q to quit \n:').casefold()
        if x == 'binary':
            return binary_checher()
        elif x == 'decimal':
            return decimal_checker()
        elif x == 'q':
            return quit()

def quit():
    """Needed to escape the script"""
    print("Let's meet again")
    exit()
def binary_checher():
    """This function is called by data_type if user inputs "binary", it takes no argument, and asks the user for a
    binary number, then proceeds to make sure the number is made of 0s and 1s only and then if the input is correct
    calls the binary_conversion function providing it with the correct argument"""
    while True:
        looper = 0
        check = []
        while looper == 0:
            x = input('Input the Binary number you want to convert in decimal (press q to exit) \n(Binary numbers only have 0s and 1s)\n:')
            if x.casefold() == 'q':
                return quit()
            try:
                x = int(x)
                for i in range(len(str(x))):
                    if 0 <= int((str(x))[i]) <= 1:
                        check.append('yes')
                    else:
                        check.append('no')
            except:
                continue

            if check and 'no' not in check:
                return binary_conversion(str(x))
            else:
                check = []

def binary_conversion(x):
    """This function doesn't need any checking, takes the binary argument and returns the same number as a decimal"""
    y = x[::-1]
    decimal = 0
    for i in range(len(y)):
        decimal += int(y[i]) * (2 ** i)
    print(f'The binary number {x} is the decimal number {decimal}')

def decimal_checker():
    """This function is called by data_type if user inputs "decimal", it takes no argument, and asks the user for a
        decimal number, then proceeds to make sure the number is made of 0s and 1s only and then if the input is correct
        calls the decimal_conversion function providing it with the correct argument"""
    while True:
        x = input("What's the Decimal number you want to convert into Binary? \n: ")
        if x.isnumeric():
            if int(x) == 0:
                break
            else:
                return decimal_conversion(x)

        else:
            print("This needs to be a number.")
    print('Decimal 0 equals to binary 0')


def decimal_conversion(init):
    x = int(init)
    binary = []
    while True:
        if x > 0:
            z = x % 2
            if z == 0:
                binary.append(0)
            else:
                binary.append(1)

            x = x // 2
        else:
            break
    binary.reverse()
    print(f'Decimal {init} equals to binary ', end='')
    for i in range(len(binary)):
        print(binary[i], end='')
    print('')


print('This program helps you in binary to decimal conversions and vice versa')
while True:
    data_type()


