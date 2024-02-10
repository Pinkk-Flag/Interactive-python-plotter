# LIBS

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

#=================
# MAIN
#=================
def startingout():
    """Prints a welcome message and brief description of the program."""
    print("Hello! Welcome to the plotter program.")
    print("This program is designed to help you plot data in various ways.")
    print("You will be prompted to enter the X values. Say END in order to stop asking for the x and to move onto the y.")
    print("You will be further given instructions")
    print("\n" * 3)

def __main__():
    """The main function that is executed when the script is run."""
    startingout()  # Call the startingout function

if __name__ == "__main__":
    __main__()


x_val = []
y_val = []

while True:
    userinputXVAL = input("Please enter your x value (type 'END' to finish): ")
    if userinputXVAL == "END":
        break
    x_val.append(userinputXVAL)

while True:
    userinputYVAL = input("Please enter your y value (type 'END' to finish): ")
    if userinputYVAL == "END":
        break
    y_val.append(userinputYVAL)

title = str(input("Please enter the title of your graph: "))
x_axis_title = str(input("Please enter the x axis title of your graph: "))
y_axis_title = str(input("Please enter the y axis title of your graph: "))

userchoice = int(input("Please enter the type of plot you want. Type [1] for a plot, [2] (type the literal number please) for scatter: "))

if userchoice == 1:
    plt.plot(x_val, y_val)
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.title(title)

    plt.show()
elif userchoice == 2:
    plt.scatter(x_val, y_val)
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.title(title)

    plt.show()
#=================
# FUNCTIONS
#=================
def linearreg():
    """Prints a message indicating linear regression functionality is not yet implemented."""
    print("Linear regression functionality is not yet implemented.")

def quadraticreg():
    """Prints a message indicating quadratic regression functionality is not yet implemented."""
    print("Quadratic regression functionality is not yet implemented.")

    

