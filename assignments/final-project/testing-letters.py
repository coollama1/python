def onlyLetters(value):
    output = ""
    for i in value:
        if i.isalpha():
            output = output + i
    return output

string = "sdako akoo 1 11320  \n\n 121o ko kako a 2     "
print(onlyLetters(string))