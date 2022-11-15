from tkinter import *
from tkinter import messagebox

expression = ""


# CLEAR FUNCTION
def clear_display():
    global expression
    display.config(state="normal")
    expression = ""
    display.delete(0, END)
    display.config(state="readonly")


# PRESS FUNCTION
def press(num):
    global expression
    display.config(state="normal")
    expression += str(num)
    display.delete(0, END)
    display.insert(0, expression)
    display.config(state="readonly")


# COMPUTE FUNCTION
def compute():
    global expression
    try:
        answer = eval(expression)
    except:
        messagebox.showerror(title="Error", message='Invalid Expression')
    else:
        display.config(state="normal")
        display.delete(0, END)
        display.insert(0, f"= {answer}")
        display.config(state="readonly")
        expression = str(answer)


# BACKSPACE FUNCTION
def backspace():
    global expression
    display.config(state="normal")
    expression = expression[0:len(expression) - 1]
    display.delete(0, END)
    display.insert(0, expression)
    display.config(state="readonly")


# UI Setup
window = Tk()
window.title("Simple Calculator")
window.config(pady=30, padx=60)

display = Entry(width=34, font=("Times New Roman", 20, "normal"), state="readonly", highlightcolor="black",
                highlightthickness=2, highlightbackground="black")
display.insert(0, "Yes")
display.grid(row=0, column=0, columnspan=5, pady=10)

button_7 = Button(text="7", width=10, height=3, command=lambda: press(7))
button_7.grid(row=1, column=0, pady=10, padx=10)
button_8 = Button(text="8", width=10, height=3, command=lambda: press(8))
button_8.grid(row=1, column=1, padx=10)
button_9 = Button(text="9", width=10, height=3, command=lambda: press(9))
button_9.grid(row=1, column=2, padx=10)
backspace_button = Button(text="Backspace", width=25, height=3, command=backspace)
backspace_button.grid(row=1, column=3, padx=10, columnspan=2)

button_4 = Button(text="4", width=10, height=3, command=lambda: press(4))
button_4.grid(row=2, column=0, pady=10, padx=10)
button_5 = Button(text="5", width=10, height=3, command=lambda: press(5))
button_5.grid(row=2, column=1, padx=10)
button_6 = Button(text="6", width=10, height=3, command=lambda: press(6))
button_6.grid(row=2, column=2, padx=10)
multiply_button = Button(text="*", width=10, height=3, command=lambda: press("*"))
multiply_button.grid(row=2, column=3, padx=10)
divide_button = Button(text="/", width=10, height=3, command=lambda: press("/"))
divide_button.grid(row=2, column=4, padx=10)

button_1 = Button(text="1", width=10, height=3, command=lambda: press(1))
button_1.grid(row=3, column=0, pady=10, padx=10)
button_2 = Button(text="2", width=10, height=3, command=lambda: press(2))
button_2.grid(row=3, column=1, padx=10)
button_3 = Button(text="3", width=10, height=3, command=lambda: press(3))
button_3.grid(row=3, column=2, padx=10)
subtract_button = Button(text="-", width=10, height=3, command=lambda: press("-"))
subtract_button.grid(row=3, column=3, padx=10)
equal_button = Button(text="=", width=10, height=8, command=compute)
equal_button.grid(row=3, column=4, rowspan=2, padx=10)

clear_button = Button(text="C", width=10, height=3, command=clear_display)
clear_button.grid(row=4, column=0, pady=10, padx=10)
button_0 = Button(text="0", width=10, height=3, command=lambda: press(0))
button_0.grid(row=4, column=1, padx=10)
dec_point = Button(text=".", width=10, height=3, command=lambda: press("."))
dec_point.grid(row=4, column=2, padx=10)
add_button = Button(text="+", width=10, height=3, command=lambda: press("+"))
add_button.grid(row=4, column=3, padx=10)

window.mainloop()
