import time
import tkinter as tk

marcados = [False, False, False, False, False, False, False, False, False]
minhas_marcacoes = [False, False, False, False, False, False, False, False, False]
ganhou = False

def jogo_da_velha():
	def janela_resultado(texto):
		def novo_jogo(root2):
			root2.quit()
			root2.destroy()
			jogo_da_velha()

		root2 = tk.Tk()
		root2.geometry("800x640")

		label = tk.Label(root2, text=texto)
		label.pack(padx=20, pady=20)

		botao_reset = tk.Button(root2, text="Reiniciar", command=lambda: novo_jogo(root2))
		botao_reset.pack(padx=10, pady=10)
		root.destroy()
		root2.mainloop()


	def marcar_botao0():
		global marcados
		global minhas_marcacoes
		button0.config(state="disabled")
		button0.config(text="X")
		marcados[0] = True
		minhas_marcacoes[0] = True
		if marcados[2] == True:
			if marcados[1] == False:
				button1.config(state="disabled")
				button1.config(text="O")
				marcados[1] = True
		if marcados[1] == True:
			if marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
		if marcados[3] == True:
			if marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
		if marcados[6] == True:
			if marcados[3] == False:
				button3.config(state="disabled")
				button3.config(text="O")
				marcados[3] = True
		if marcados[4] == True:
			if marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
		if marcados[8] == True:
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True

		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao1():
		global marcados
		global minhas_marcacoes
		button1.config(state="disabled")
		button1.config(text="X")
		marcados[1] = True
		minhas_marcacoes[1] = True
		if marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
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
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao2():
		global marcados
		global minhas_marcacoes
		button2.config(state="disabled")
		button2.config(text="X")
		marcados[2] = True
		minhas_marcacoes[2] = True
		if marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
		elif marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
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
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao3():
		global marcados
		global minhas_marcacoes
		button3.config(state="disabled")
		button3.config(text="X")
		marcados[3] = True
		minhas_marcacoes[3] = True
		if marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
		elif marcados[6] == False:
			button6.config(state="disabled")
			button6.config(text="O")
			marcados[6] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
		elif marcados[8] == False:
			button8.config(state="disabled")
			button8.config(text="O")
			marcados[8] = True
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao4():
		global marcados
		global minhas_marcacoes
		button4.config(state="disabled")
		button4.config(text="X")
		marcados[4] = True
		minhas_marcacoes[4] = True
		if marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[6] == False:
			button6.config(state="disabled")
			button6.config(text="O")
			marcados[6] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		elif marcados[8] == False:
			button8.config(state="disabled")
			button8.config(text="O")
			marcados[8] = True
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao5():
		global marcados
		global minhas_marcacoes
		button5.config(state="disabled")
		button5.config(text="X")
		marcados[5] = True
		minhas_marcacoes[5] = True
		if marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[8] == False:
			button8.config(state="disabled")
			button8.config(text="O")
			marcados[8] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
		elif marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
		elif marcados[6] == False:
			button6.config(state="disabled")
			button6.config(text="O")
			marcados[6] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao6():
		global marcados
		global minhas_marcacoes
		button6.config(state="disabled")
		button6.config(text="X")
		marcados[6] = True
		minhas_marcacoes[6] = True
		if marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao7():
		global marcados
		global minhas_marcacoes
		button7.config(state="disabled")
		button7.config(text="X")
		marcados[7] = True
		minhas_marcacoes[7] = True
		if marcados[6] == False:
			button6.config(state="disabled")
			button6.config(text="O")
			marcados[6] = True
		elif marcados[8] == False:
			button8.config(state="disabled")
			button8.config(text="O")
			marcados[8] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

	def marcar_botao8():
		global marcados
		global minhas_marcacoes
		button8.config(state="disabled")
		button8.config(text="X")
		marcados[8] = True
		minhas_marcacoes[8] = True
		if marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
		elif marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
		elif marcados[6] == False:
			button6.config(state="disabled")
			button6.config(text="O")
			marcados[6] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			janela_resultado("Você ganhou!")

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
if __name__ == "__main__":
	jogo_da_velha()
