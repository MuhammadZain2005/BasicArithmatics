# Program 1
# This program executes the basic arithmetics operations with two user-given inputs

class color:  # Color Class
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print(
    color.UNDERLINE + color.BOLD + color.GREEN + "****basic arithmatic operations****".upper() + color.END + color.END + color.END)
print(
    color.BLUE + "This program performs addition, substraction, division,and multiplication for any user-given two integers")

input1 = float(input("\nplease input the first number = ".title()))
input2 = float(input("please input the second number = ".title()))


def addition(number1, number2):
    return number1 + number2


def substraction(number1a, number2a):
    return number1a - number2a


def division(number1b, number2b):
    return number1b / number2b


def multiplication(number1c, number2c):
    return number1c * number2c


print("\nThe addition of both numbers is " + str(addition(input1, input2)))
print("The substraction of both numbers is " + str(substraction(input1, input2)))
print("The division of both numbers is " + str(round(division(input1, input2), 2)))
print("The multiplication of both numbers is " + str(multiplication(input1, input2)))

print(color.GREEN + "\nMade by Muhammad Zain" + color.END)
