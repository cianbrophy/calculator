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

    window.configure(background ="white")

    window.title("Cian's Calculator™")

    window.geometry("380x450")

    equation = StringVar()

    value_field = Entry(window, textvariable = equation)

    value_field.grid(columnspan = 4, ipadx = 50)

    equation.set('enter your value')

    button1 = Button(window, text=' 1 ', fg='black', bg='white', 
                     command=lambda: press(1), height=5, width=10) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(window, text=' 2 ', fg='black', bg='white', 
                     command=lambda: press(2), height=5, width=10) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(window, text=' 3 ', fg='black', bg='white', 
                     command=lambda: press(3), height=5, width=10) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(window, text=' 4 ', fg='black', bg='white', 
                     command=lambda: press(4), height=5, width=10) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(window, text=' 5 ', fg='black', bg='white', 
                     command=lambda: press(5), height=5, width=10) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(window, text=' 6 ', fg='black', bg='white', 
                     command=lambda: press(6), height=5, width=10) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(window, text=' 7 ', fg='black', bg='white', 
                     command=lambda: press(7), height=5, width=10) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(window, text=' 8 ', fg='black', bg='white', 
                     command=lambda: press(8), height=5, width=10) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(window, text=' 9 ', fg='black', bg='white', 
                     command=lambda: press(9), height=5, width=10) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(window, text=' 0 ', fg='black', bg='white', 
                     command=lambda: press(0), height=5, width=10) 
    button0.grid(row=5, column=0) 
  
    plus = Button(window, text=' + ', fg='black', bg='white', 
                  command=lambda: press("+"), height=5, width=10) 
    plus.grid(row=2, column=3) 
  
    minus = Button(window, text=' - ', fg='black', bg='white', 
                   command=lambda: press("-"), height=5, width=10) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(window, text=' × ', fg='black', bg='white', 
                      command=lambda: press("*"), height=5, width=10) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(window, text=' ÷ ', fg='black', bg='white', 
                    command=lambda: press("/"), height=5, width=10) 
    divide.grid(row=5, column=3) 
  
    equal = Button(window, text=' = ', fg='black', bg='white', 
                   command=equalpress, height=5, width=10) 
    equal.grid(row=5, column=2) 
  
    clear = Button(window, text='CLR', fg='black', bg='white', 
                   command=clear, height=5, width=10) 
    clear.grid(row=5, column='1') 
  
    Decimal= Button(window, text='.', fg='black', bg='white', 
                    command=lambda: press('.'), height=5, width=10) 
    Decimal.grid(row=6, column=0) 
    
    window.mainloop() 