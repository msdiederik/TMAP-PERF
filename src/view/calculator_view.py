"""Module for configuring the view of the calculator"""
from tkinter import Tk, Entry, Button
import calculation_service as calculation_service


def initialize_calculator():
    """Function to initialize the frontend"""

    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window to Calculator
    gui.title("TMAP Calculator")

    # set the configuration of GUI window
    gui.geometry("400x200")

    # Initialize an object of the CalculationService class
    service = calculation_service.CalculationService()

    # set whats shown on the calculator screen to the equation, and initialize that to started
    expression_field = Entry(gui, textvariable=service.get_equation())
    service.set_equation('started')

    # create a grid in order to put buttons in
    expression_field.grid(columnspan=4, ipadx=70)


    # create all the buttons
    button1 = Button(gui, text=' 1 ', fg='black',
                     bg='red', command=lambda: service.press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black',
                     bg='red', command=lambda: service.press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black',
                     bg='red', command=lambda: service.press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black',
                     bg='red',command=lambda: service.press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black',
                     bg='red',command=lambda: service.press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black',
                     bg='red', command=lambda: service.press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black',
                     bg='red', command=lambda: service.press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black',
                     bg='red', command=lambda: service.press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black',
                     bg='red', command=lambda: service.press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black',
                     bg='red', command=lambda: service.press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black',
                  bg='red', command=lambda: service.press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black',
                   bg='red',  command=lambda: service.press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black',
                      bg='red', command=lambda: service.press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black',
                    bg='red', command=lambda: service.press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black',
                   bg='red', command=lambda: service.equalpress(), height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black',
                   bg='red', command=lambda: service.clear(), height=1, width=7)
    clear.grid(row=5, column='1')

    decimal = Button(gui, text='.', fg='black',
                     bg='red',command=lambda: service.press('.'), height=1, width=7)
    decimal.grid(row=6, column=0)

    # start program loop
    gui.mainloop()
