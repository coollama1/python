from tkinter import *
from tkinter import ttk

def printThings():
    global entry
    global number_of_letters
    global root
    input = entry.get()
    output = int(input)
    root.destroy

root = Tk()
number_of_letters = 0

root.title("Accepting Input")
prompt = Label(root, text = "Number of Letters (n): ")
entry = Entry(root) 
button = Button(root, text = "Submit", command = lambda:[printThings(),root.destroy()])

prompt.grid(row = 0, column = 0, sticky = W, padx = 4)
entry.grid(row = 0, column = 1, sticky = E, pady = 4)
entry.focus_set()
button.grid(row = 0, column = 4)

root.mainloop()


#part 1 - the button
"""
root.title("First GUI")
ttk.Button(root, text = "Hello World").grid()
"""

#part 2 - the label/frame
"""
frame = Frame(root)

labelText = StringVar()

label = Label(frame, textvariable = labelText)
button = Button(frame, text = "click me")

labelText.set("I am a label")

label.pack()
button.pack()
frame.pack()
"""

#part 3 - positioning with pack() 
"""
frame = Frame(root)

Label(frame, text = "Why am I even doing this").pack()

Button(frame, text = "A1").pack(side = LEFT, fill = Y)
Button(frame, text = "A2").pack(side = TOP, fill = X)
Button(frame, text = "A3").pack(side = RIGHT, fill = X)
Button(frame, text = "A4").pack(side = LEFT, fill = X)

frame.pack()
"""

#part 4 - text inputs/positioning with grid()
"""
Label(root, text = "First Name").grid(row = 0, sticky = W, padx = 4)
Entry(root).grid(row = 0, column = 1, sticky = E, pady = 4)

Label(root, text = "Last Name").grid(row = 1, sticky = W, padx = 4)
Entry(root).grid(row = 1, column = 1, sticky = E, pady = 4)

Button(root, text = "Submit").grid(row = 3)
"""

#part 5 - radiobutton
"""
Label(root, text = "Height").grid(row = 0, column = 0, sticky = W)
Entry(root, width = 50).grid(row = 0, column = 1)
Button(root, text = "Submit").grid(row = 0, column = 8)

Label(root, text = "Size").grid(row = 1, column = 0, sticky = W)
Radiobutton(root, text = "Inches", value = 2).grid(row = 2, column = 0, sticky = W)
Radiobutton(root, text = "Centermeters", value = 3).grid(row = 3, column = 0, sticky = W)
Radiobutton(root, text = "Milimmeters", value = 4).grid(row = 4, column = 0, sticky = W)
Radiobutton(root, text = "Kilometers", value = 5).grid(row = 5, column = 0, sticky = W)
"""