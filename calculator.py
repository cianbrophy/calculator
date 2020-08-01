from tkinter import *

value = ""

def press(num):
    global value

    value = value + str(num)

    equation.set(value)


def equalpress():

    try:
        global value

        total = str(eval(value))

        equation.set(total)

        value = ""

    except:
        equation.set("error")
        value = ""


def clear():
    global value
    value = ""
    equation.set("")


if __name__ == "__main__":

    window = Tk()

    window.configure(background ="black")

    window.title("Calculator")

    window.geometry("800x600")



