from tkinter import *
from customtkinter import *
expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:

		equation.set(" error ")
		expression = ""
def clear():
	global expression
	expression = ""
	equation.set("")


if __name__ == "__main__":
	root = CTk()
	root.title("Simple Calculator")
	root.geometry("270x150")
	equation = StringVar()
	expression_field = CTkEntry(root, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = CTkButton(root, text=' 1 ',command=lambda: press(1), height=20, width=50)
	button1.grid(row=2, column=0)
	button2 = CTkButton(root, text=' 2 ',command=lambda: press(2), height=20, width=50)
	button2.grid(row=2, column=1)
	button3 = CTkButton(root, text=' 3 ',command=lambda: press(3), height=20, width=50)
	button3.grid(row=2, column=2)
	button4 = CTkButton(root, text=' 4 ',command=lambda: press(4), height=20, width=50)
	button4.grid(row=3, column=0)
	button5 = CTkButton(root, text=' 5 ',command=lambda: press(5), height=20, width=50)
	button5.grid(row=3, column=1)
	button6 = CTkButton(root, text=' 6 ',command=lambda: press(6), height=20, width=50)
	button6.grid(row=3, column=2)
	button7 = CTkButton(root, text=' 7 ',command=lambda: press(7), height=20, width=50)
	button7.grid(row=4, column=0)
	button8 = CTkButton(root, text=' 8 ',command=lambda: press(8), height=20, width=50)
	button8.grid(row=4, column=1)
	button9 = CTkButton(root, text=' 9 ',command=lambda: press(9), height=20, width=50)
	button9.grid(row=4, column=2)
	button0 = CTkButton(root, text=' 0 ',command=lambda: press(0), height=20, width=50)
	button0.grid(row=5, column=0)
	plus = CTkButton(root, text=' + ',command=lambda: press("+"), height=20, width=50)
	plus.grid(row=2, column=3)
	minus = CTkButton(root, text=' - ',command=lambda: press("-"), height=20, width=50)
	minus.grid(row=3, column=3)
	multiply = CTkButton(root, text=' * ',command=lambda: press("*"), height=20, width=50)
	multiply.grid(row=4, column=3)
	divide = CTkButton(root, text=' / ', command=lambda: press("/"), height=20, width=50)
	divide.grid(row=5, column=3)
	equal = CTkButton(root, text=' = ', command=equalpress, height=20, width=50)
	equal.grid(row=5, column=2)
	clear = CTkButton(root, text='Clear',command=clear, height=20, width=50)
	clear.grid(row=5, column='1')
	Decimal= CTkButton(root, text='.', command=lambda: press('.'), height=20, width=50)
	Decimal.grid(row=6, column=0)
	root.mainloop()
