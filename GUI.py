from tkinter import *


def btnclick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)


def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")


def btnClick_Equal():
    global operator
    Equal = str(eval(operator))
    text_input.set(Equal)
    # operator = ""


window = Tk()
window.title("Calculator")
operator = ""
text_input = StringVar()
Display = Entry(window, font=('arial', 20, "bold"), textvariable=text_input, bd=30, insertwidth=1,
                bg="powder blue",
                justify="right").grid(columnspan=4)
btn7 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="7",
              command=lambda: btnclick(7)).grid(
    row=1,
    column=0)

btn8 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="8",
              command=lambda: btnclick(8)).grid(
    row=1,
    column=1)

btn9 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="9",
              command=lambda: btnclick(9)).grid(
    row=1,
    column=2)

Addition = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"),
                  text="+", command=lambda: btnclick("+")).grid(row=1,
                                                                column=3)
# ==============================================================================================================================
btn4 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="4",
              command=lambda: btnclick(4)).grid(
    row=2,
    column=0)

btn5 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="5",
              command=lambda: btnclick(5)).grid(
    row=2,
    column=1)

btn6 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="6",
              command=lambda: btnclick(6)).grid(
    row=2,
    column=2)

subtraction = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"),
                     text="-", command=lambda: btnclick("-")).grid(
    row=2,
    column=3)
# ==============================================================================================================================
btn1 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="1",
              command=lambda: btnclick(1)).grid(
    row=3,
    column=0)

btn2 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="2",
              command=lambda: btnclick(2)).grid(
    row=3,
    column=1)

btn3 = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="3",
              command=lambda: btnclick(3)).grid(
    row=3,
    column=2)

multiply = Button(window, padx=16, bd=8, pady=16, bg="powder blue", fg="black", font=('arial', 20, "bold"),
                  text="*", command=lambda: btnclick("*")).grid(
    row=3,
    column=3)
# ==============================================================================================================================
btn0 = Button(window, padx=16, pady=16, bd=8, bg="powder blue", fg="black", font=('arial', 20, "bold"), text="0",
              command=lambda: btnclick(0)).grid(
    row=4,
    column=0)

btn_clear = Button(window, padx=16, pady=16, bd=8, bg="powder blue", fg="black", font=('arial', 20, "bold"),
                   text="C", command=btncleardisplay).grid(row=4,
                                                           column=1)

btn_equal = Button(window, padx=16, pady=16, bd=8, bg="powder blue", fg="black", font=('arial', 20, "bold"),
                   text="=", command=btnClick_Equal).grid(row=4,
                                                          column=2)

division = Button(window, padx=16, pady=16, bd=8, bg="powder blue", fg="black", font=('arial', 20, "bold"),
                  text="/", command=lambda: btnclick("/")).grid(
    row=4,
    column=3)
window.mainloop()
