  
#Author: Gregory Grizzle
#Date Created: 4/20/2022
#Course:ITT103
#Purpose:  


# Import everything from the tkinter package
# to provide the GUI
from tkinter import *

# Create the tk window
top = Tk()
# Set the title of the window
top.title("JamEx Rate Calculator")

# Create a label that is contained within the tk window
# This displays text
# and aligns the text within the label to the left
L1 = Label(top, text="Sales Person Number", justify=LEFT)
# Place the lable in the top left corner of the window
# and align the label to the left
L1.grid(sticky="W",row=0,column=0)

# This creates an input field
lb_num= Entry(top,bd=5)
lb_num.grid(row=0,column=1)

L2= Label(top, text="Sales Amount", justify=LEFT)
L2.grid(sticky="W",row=1,column=0)

lb_amount= Entry(top,bd=5)
lb_amount.grid(row=1,column=1)

L3= Label(top, text="Sales Person Class", justify=LEFT)
L3.grid(sticky="W",row=2,column=0)

# This stores the values that can be chosen in the dropdown menu
classes = [
    1,2,3
]

# This creates the variable that will store the chosen class
chosen_class = StringVar(top)
# Set the default value of the variable to the first option
chosen_class.set(classes[0])

# This create the dropdown menu and sets its options
lb_class= OptionMenu(top,chosen_class,*classes)
lb_class.grid(row=2,column=1)

L4= Label(top, text="Comission Rate", justify=LEFT)
L4.grid(sticky="W",row=3,column=0)

lb_rate= Label(top, text="")
lb_rate.grid(row=3,column=1)

# This function works like isdigit in determining whether
# a value can be converted to a float without error
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# This function calculates and displays the rate
def getRate():
    num = 0
    amount = 0
    sp_class = 0
    rate = 0

    if lb_num.get().isdigit():
        num = int(lb_num.get())
        # Set the rate label text to a new value
        lb_rate.config(text="")
    else:
        lb_rate.config(text="Invalid Sales Person Number")
        return

    if isfloat(lb_amount.get()):
        amount = float(lb_amount.get())
        lb_rate.config(text="")
    else:
        lb_rate.config(text="Please Enter Sales Amount")
        return
    
    # The chosen class will return a string regardless
    # so the value must be converted back into an integer
    sp_class = int(chosen_class.get())

    if sp_class == 1 :
        if amount <= 1000 :
            rate = 6
        elif amount > 1000 and amount < 2000 :
            rate = 7
        elif amount >= 2000 :
            rate = 10
    elif sp_class == 2 :
        if amount < 1000 :
            rate = 4
        elif amount >= 1000 :
            rate = 6
    elif sp_class == 3 :
        rate = 4.5

    # To display the rate it must be converted into a string
    lb_rate.config(text=str(rate))

# This creates a button and set the function called when clicked
# to exit
btn_exit = Button(top, text="Exit", command=exit)
btn_exit.grid(row=4,column=0)

# This button is set to call the getRate function
# which wil calculate the rate
button = Button(top, text="Calculate Rate", command=getRate)
button.grid(row=4,column=1)

# Show and enable the tk window
top.mainloop()
