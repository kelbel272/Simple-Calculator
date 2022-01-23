from tkinter import *

# Open up window 
root = Tk()

#Create title for window 
root.title("Simple Calculator")

# Create entry widget 
e = Entry(root, width=35, borderwidth=1)

#Create entry grid 
#Columnspan has it span across all 4 columns 
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5) #display entry 

# Adds number to the entry display when clicked 
def button_click(number):
    current = e.get()   #insert the number clicked 
    e.delete(0, END) # delete previous number (if needed)
    e.insert(0, str(current) + str(number))   # display numbers in order clicked as a string

# Clears out the calculator 
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)



#Create buttons 
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=60, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=20, pady=53, command=button_add)
button_equal = Button(root, text="=", padx=20, pady=53, command=button_equal)
button_clear = Button(root, text="C", padx=20, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=21, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=21, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=22, pady=20, command=button_divide)

# Display the buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2)

button_add.grid(row=2, column=3, rowspan=2)
button_equal.grid(row=4, column=3, rowspan=2)
button_subtract.grid(row=1, column=3)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=1, column=1)


# event listener for window 
root.mainloop()