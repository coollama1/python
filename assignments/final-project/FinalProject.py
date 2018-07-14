from tkinter import *
import turtle
import random
import math

# Create and populate a file
my_file = open("Words.txt", "w");
print(
    """This is a haiku,
    Watch close to the syllables,
    Before it is done.""",
    file=my_file
);
my_file.close();

# Helper Functions

def onlyLetters(value):
    output = ""
    for i in value:
        if i.isalpha():
            output = output + i
    return output

def letterChart(fileName):
    ''' Returns a dictionary of the frequency of every letter in a given file.'''
    letterFrequency = {};
    temp_file = open(fileName, "r");
    current_line = temp_file.readline();
    while(current_line != ""):
            for letter in current_line:
                if not letter in letterFrequency:
                    letterFrequency[letter] = 1;
                else:
                    letterFrequency[letter] += 1;
            current_line = temp_file.readline();
    return letterFrequency;

def modifiedList(number, mydict):
    '''Returns a list of n largest values in a given dictionary'''
    return sorted(mydict.items(), key=lambda x:-x[1])[:number];

def allOtherLetters(myList, total):
    for letters in myList:
        total = total - letters[1];
    return total;

def angle(percent):
    ''' Updates the percent to an angle angle'''
    return percent*360;

def percentage(total, value):
    ''' returns the percentage of the value from the total'''
    return value/total;

def generateNewColor():
    '''generates a new hex-value color'''
    color = lambda: random.randint(0,255)
    return '#{:02x}{:02x}{:02x}'.format(color(),color(),color())

def makeArc(t, color, angle):
    t.fillcolor(color);
    t.begin_fill();
    t.circle(120, angle);
    position = t.position();
    t.goto(0, 0);
    t.end_fill();
    t.setposition(position);

def makeLabel(t, label, angle):
    t.circle(150, angle/ 2)
    t.write(label, align="center")
    t.circle(150, angle/ 2)
    

def printThings():
    global entry;
    global number_of_letters;
    global root;
    input = entry.get();
    number_of_letters = int(input);
    #root.destroy
    drawCircle("Words.txt");

def drawCircle(filename):
    myDict = letterChart(filename);
    totalSum = sum(myDict.values());
    myList = modifiedList(number_of_letters, myDict);
    myList.append(('All other letters', allOtherLetters(myList, totalSum)));
        
    myTurtle = turtle.Turtle();
    myTurtle2 = turtle.Turtle();
    myTurtle.penup();
    myTurtle2.penup();
    myTurtle.sety(-120);
    myTurtle2.sety(-150)
    myTurtle.pendown();
    
    for letters in myList:
        percent = percentage(totalSum, letters[1]);
        wordAngle = angle(percent);
        label= letters[0] + ", " + str(round(percent, 4));
        makeArc(myTurtle, generateNewColor(), wordAngle);
        makeLabel(myTurtle2, label, wordAngle)

root = Tk();
number_of_letters = 0;

root.title("Accepting Input");
prompt = Label(root, text="Number of Letters (n): ");
entry = Entry(root);
button = Button(root, text="Submit", command=lambda: [printThings(),root.destroy()]);
prompt.grid(row=0, column=0, sticky=W, padx=4);
entry.grid(row=0, column=1, sticky=E, pady=4);
entry.focus_set();
button.grid(row=0, column=4);
root.mainloop();
