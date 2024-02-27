import tkinter
import math

#global equation
equation = ""
#buttons to each integer
def pressed_1():
    global equation
    equation = equation + "1"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_2():
    global equation
    equation = equation + "2"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_3():
    global equation
    equation = equation + "3"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_4():
    global equation
    equation = equation + "4"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_5():
    global equation
    equation = equation + "5"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_6():
    global equation
    equation = equation + "6"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_7():
    global equation
    equation = equation + "7"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_8():
    global equation
    equation = equation + "8"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_9():
    global equation
    equation = equation + "9"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_0():
    #handles multiple 0's in beginning equation
    global equation
    equation = equation + "0"
    while equation.startswith("00"):
        equation= equation[1:]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_equal():
    #handles multiple 0's in beginning equation
    global equation
    entry_text = screen.get()
    equation = entry_text
    equation = eval(equation)
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()
    equation = ""

def pressed_plus():
    global equation
    equation = equation + "+"
    if equation.startswith("+"):
        equation= equation[1:]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_minus():
    global equation
    equation = equation + "-"
    if equation.startswith("-"):
        equation= equation[1:]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_x():
    global equation
    equation = equation + "*"
    if equation.startswith("*"):
        equation= equation[1:]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_div():
    global equation
    equation = equation + "/"
    if equation.startswith("/"):
        equation= equation[1:]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_pow():
    global equation
    equation = equation + "**"
    if equation.startswith("**"):
        equation= equation[1:]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_sqrt():
    global equation
    equation = math.sqrt(eval(equation))
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_par():
    #handles many bracket situations
    global equation
    if equation.endswith("+"):
        equation = equation + "("
    if equation.endswith("-"):
        equation = equation + "("
    if equation.endswith("*"):
        equation = equation + "("
    if equation.endswith("/"):
        equation = equation + "("
    if equation.endswith("**"):
        equation = equation + "("
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_endpar():
    # handles closing bracket situations
    global equation
    # check if there is an open bracket
    for letter in equation:
        if letter == '(':
            equation = equation + ")"
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_clear():
    global equation
    equation = ""
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

def pressed_clearle():
    global equation
    equation = equation[0:-1]
    screen.delete(0, tkinter.END)
    screen.insert(0, equation)
    screen.update()

if __name__=='__main__':
    #creates main window
    window = tkinter.Tk()
    window.title("Calculator")
    window.geometry("640x480")
    window.resizable(False, False)
    #frame for screen
    frame = tkinter.Frame(window, bg="lightgray", height=0, pady=50, padx=0)
    frame.grid(row=1, column=0, columnspan=4, sticky="nsew")
    screen = tkinter.Entry(frame, textvariable=equation, width=88, highlightcolor='white', font=("Arial", 16))
    screen.grid(row=0, column=0, columnspan=4, sticky="nsew")
    #put buttons
    botao1 = tkinter.Button(text="1", command=pressed_1, width=10)
    botao1.place(relx=0.05, rely=0.3)
    botao2 = tkinter.Button(text="2", command=pressed_2, width=10)
    botao2.place(relx=0.20, rely=0.3)
    botao3 = tkinter.Button(text="3", command=pressed_3, width=10)
    botao3.place(relx=0.35, rely=0.3)
    botao4 = tkinter.Button(text="4", command=pressed_4, width=10)
    botao4.place(relx=0.05, rely=0.4)
    botao5 = tkinter.Button(text="5", command=pressed_5, width=10)
    botao5.place(relx=0.20, rely=0.4)
    botao6 = tkinter.Button(text="6", command=pressed_6, width=10)
    botao6.place(relx=0.35, rely=0.4)
    botao7 = tkinter.Button(text="7", command=pressed_7, width=10)
    botao7.place(relx=0.05, rely=0.5)
    botao8 = tkinter.Button(text="8", command=pressed_8, width=10)
    botao8.place(relx=0.20, rely=0.5)
    botao9 = tkinter.Button(text="9", command=pressed_9, width=10)
    botao9.place(relx=0.35, rely=0.5)
    botao0 = tkinter.Button(text="0", command=pressed_0, width=10)
    botao0.place(relx=0.20, rely=0.6)
    botao_equal = tkinter.Button(text="=", command=pressed_equal, width=10)
    botao_equal.place(relx=0.35, rely=0.6)
    botao_plus = tkinter.Button(text="+", command=pressed_plus, width=10)
    botao_plus.place(relx=0.50, rely=0.3)
    botao_minus = tkinter.Button(text="-", command=pressed_minus, width=10)
    botao_minus.place(relx=0.50, rely=0.4)
    botao_x = tkinter.Button(text="x", command=pressed_x, width=10)
    botao_x.place(relx=0.50, rely=0.5)
    botao_div = tkinter.Button(text="/", command=pressed_div, width=10)
    botao_div.place(relx=0.65, rely=0.3)
    botao_pow = tkinter.Button(text="^", command=pressed_pow, width=10)
    botao_pow.place(relx=0.65, rely=0.4)
    botao_sqrt = tkinter.Button(text="sqrt", command=pressed_pow, width=10)
    botao_sqrt.place(relx=0.65, rely=0.5)
    botao_par = tkinter.Button(text="(", command=pressed_par, width=10)
    botao_par.place(relx=0.80, rely=0.3)
    botao_endpar = tkinter.Button(text=")", command=pressed_endpar, width=10)
    botao_endpar.place(relx=0.80, rely=0.4)
    botao_clear = tkinter.Button(text="C", command=pressed_clear, width=10)
    botao_clear.place(relx=0.80, rely=0.5)
    botao_clearle = tkinter.Button(text="CLE", command=pressed_clearle, width=10)
    botao_clearle.place(relx=0.80, rely=0.6)
    #mainwindow loop
    window.mainloop()
