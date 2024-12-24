import tkinter as tk

marcados = [False, False, False, False, False, False, False, False, False,]

def marcar_botao0():
	global turno
	global marcados
	button0.config(state="disabled")
	button0.config(text="X")
	marcados[0] == True
	if marcados[1] == False:
		button1.config(state="disabled")
		button1.config(text="O")
		marcados[1] = True
	elif marcados[3] == False:
		button3.config(state="disabled")
		button3.config(text="O")
		marcados[3] = True
	elif marcados[4] == False:
		button4.config(state="disabled")
		button4.config(text="O")
		marcados[4] = True
	elif marcados[2] == False:
		button2.config(state="disabled")
		button2.config(text="O")
		marcados[2] = True
	elif marcados[5] == False:
		button5.config(state="disabled")
		button5.config(text="O")
		marcados[5] = True
	elif marcados[6] == False:
		button6.config(state="disabled")
		button6.config(text="O")
		marcados[6] = True
	elif marcados[7] == False:
		button7.config(state="disabled")
		button7.config(text="O")
		marcados[7] = True
	elif marcados[8] == False:
		button8.config(state="disabled")
		button8.config(text="O")
		marcados[8] = True

def marcar_botao1():
	global turno
	button1.config(state="disabled")
	button1.config(text="X")
	marcados[1] = True

def marcar_botao2():
	global turno
	global marcados
	button2.config(state="disabled")
	button2.config(text="X")
	marcados[2] = True

def marcar_botao3():
	global turno
	button3.config(state="disabled")
	button3.config(text="X")
	marcados[3] = True

def marcar_botao4():
	global turno
	button4.config(state="disabled")
	button4.config(text="X")
	marcados[4] = True

def marcar_botao5():
	global turno
	button5.config(state="disabled")
	button5.config(text="X")
	marcados[5] = True

def marcar_botao6():
	global turno
	button6.config(state="disabled")
	button6.config(text="X")
	marcados[6] = True

def marcar_botao7():
	global turno
	button7.config(state="disabled")
	button7.config(text="X")
	marcados[7] = True

def marcar_botao8():
	global turno
	button8.config(state="disabled")
	button8.config(text="X")
	marcados[8] = True

root = tk.Tk()
root.geometry("800x640")

button0 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao0)
button0.grid(column=1, row=0)

button1 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao1)
button1.grid(column=2, row=0)

button2 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao2)
button2.grid(column=3, row=0)

button3 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao3)
button3.grid(column=1, row=1)

button4 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao4)
button4.grid(column=2, row=1)

button5 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao5)
button5.grid(column=3, row=1)

button6 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao6)
button6.grid(column=1, row=2)

button7 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao7)
button7.grid(column=2, row=2)

button8 = tk.Button(root, text="", width=20, height=10, font= ("arial", 16), command=marcar_botao8)
button8.grid(column=3, row=2)

root.mainloop()
