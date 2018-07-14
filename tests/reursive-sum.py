
def sum(number):
    if(number == 0):
        return number
    return number + sum(number - 1)

number_string = input("Input a number :)\n")
print("The function sum is", sum(int(number_string)))