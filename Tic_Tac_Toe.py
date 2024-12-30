import tkinter as tk
import sys

marcados = [False, False, False, False, False, False, False, False, False]
minhas_marcacoes = [False, False, False, False, False, False, False, False, False]
marcacoes_computador = [False, False, False, False, False, False, False, False, False]
vitoria_jogador = False
vitoria_computador = False
#se ganhou == False and marcados == True...

def jogo_da_velha():
	def sair():
		sys.exit()

	def movimento_computador():
		global marcados
		global minhas_marcacoes
		global marcacoes_computador
		#bloqueia jogador primeiramente
		#primeira linha
		if ((minhas_marcacoes[0] == True and minhas_marcacoes[1] == True) or (minhas_marcacoes[1] == True and minhas_marcacoes[2] == True) or (minhas_marcacoes[0] == True and minhas_marcacoes[2] == True)) and (marcados[0] == False or marcados[1] == False or marcados[2] == False):
			print("1")
			if marcados[0] == False:
				button0.config(state="disabled")
				button0.config(text="O")
				marcados[0] = True
				marcacoes_computador[0] = True
			elif marcados[1] == False:
				button1.config(state="disabled")
				button1.config(text="O")
				marcados[1] = True
				marcacoes_computador[1] = True
			elif marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
				marcacoes_computador[2] = True
		#segunda linha
		elif ((minhas_marcacoes[3] == True and minhas_marcacoes[4] == True) or (minhas_marcacoes[4] == True and minhas_marcacoes[5] == True) or (minhas_marcacoes[3] == True and minhas_marcacoes[5] == True)) and (marcados[3] == False or marcados[4] == False or marcados[5] == False):
			print("oi")
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[3] == False:
				button3.config(state="disabled")
				button3.config(text="O")
				marcados[3] = True
				marcacoes_computador[3] = True
			elif marcados[5] == False:
				button5.config(state="disabled")
				button5.config(text="O")
				marcados[5] = True
				marcacoes_computador[5] = True
		#terceira linha
		elif ((minhas_marcacoes[6] == True and minhas_marcacoes[7] == True) or (minhas_marcacoes[7] == True and minhas_marcacoes[8] == True) or (minhas_marcacoes[6] == True and minhas_marcacoes[8] == True)) and (marcados[6] == False or marcados[7] == False or marcados[8] == False):
			if marcados[7] == False:
				button7.config(state="disabled")
				button7.config(text="O")
				marcados[7] = True
				marcacoes_computador[7] = True
			elif marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
				marcacoes_computador[6] = True
			elif marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
				marcacoes_computador[8] = True
		#diagonal principal
		elif ((minhas_marcacoes[0] == True and minhas_marcacoes[4] == True) or (minhas_marcacoes[4] == True and minhas_marcacoes[8] == True) or (minhas_marcacoes[0] == True and minhas_marcacoes[8] == True)) and (marcados[0] == False or marcados[4] == False or marcados[8] == False):
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[0] == False:
				button0.config(state="disabled")
				button0.config(text="O")
				marcados[0] = True
				marcacoes_computador[0] = True
			elif marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
				marcacoes_computador[8] = True
		# diagonal secundária
		elif ((minhas_marcacoes[2] == True and minhas_marcacoes[4] == True) or (minhas_marcacoes[4] == True and minhas_marcacoes[6] == True) or (minhas_marcacoes[2] == True and minhas_marcacoes[6] == True)) and (marcados[2] == False or marcados[4] == False or marcados[6] == False):
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
				marcacoes_computador[2] = True
			elif marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
				marcacoes_computador[6] = True
		# primeira coluna
		elif ((minhas_marcacoes[0] == True and minhas_marcacoes[3] == True) or (minhas_marcacoes[3] == True and minhas_marcacoes[6] == True) or (minhas_marcacoes[0] == True and minhas_marcacoes[6] == True)) and (marcados[0] == False or marcados[3] == False or marcados[6] == False):
			if marcados[3] == False:
				button3.config(state="disabled")
				button3.config(text="O")
				marcados[3] = True
				marcacoes_computador[3] = True
			elif marcados[0] == False:
				button0.config(state="disabled")
				button0.config(text="O")
				marcados[0] = True
				marcacoes_computador[0] = True
			elif marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
				marcacoes_computador[6] = True
		# segunda coluna
		elif ((minhas_marcacoes[1] == True and minhas_marcacoes[4] == True) or (minhas_marcacoes[4] == True and minhas_marcacoes[7] == True) or (minhas_marcacoes[1] == True and minhas_marcacoes[7] == True)) and (marcados[1] == False or marcados[4] == False or marcados[7] == False):
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[1] == False:
				button1.config(state="disabled")
				button1.config(text="O")
				marcados[1] = True
				marcacoes_computador[1] = True
			elif marcados[7] == False:
				button7.config(state="disabled")
				button7.config(text="O")
				marcados[7] = True
				marcacoes_computador[7] = True
		# terceira coluna
		elif ((minhas_marcacoes[2] == True and minhas_marcacoes[5] == True) or (minhas_marcacoes[5] == True and minhas_marcacoes[8] == True) or (minhas_marcacoes[2] == True and minhas_marcacoes[8] == True)) and (marcados[2] == False or marcados[5] == False or marcados[8] == False):
			if marcados[5] == False:
				button5.config(state="disabled")
				button5.config(text="O")
				marcados[5] = True
				marcacoes_computador[5] = True
			elif marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
				marcacoes_computador[2] = True
			elif marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
				marcacoes_computador[8] = True


		#faz a jogada
		# linha do meio
		elif (minhas_marcacoes[3] == False and minhas_marcacoes[4] == False and minhas_marcacoes[5] == False) and (marcados[3] == False or marcados[4] == False or marcados[5] == False):
			print("1")
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[3] == False:
				button3.config(state="disabled")
				button3.config(text="O")
				marcados[3] = True
				marcacoes_computador[3] = True
			elif marcados[5] == False:
				button5.config(state="disabled")
				button5.config(text="O")
				marcados[5] = True
				marcacoes_computador[5] = True
		#diagonal principal
		elif (minhas_marcacoes[0] == False and minhas_marcacoes[4] == False and minhas_marcacoes[8] == False) and (marcados[0] == False or marcados[4] == False or marcados[8] == False):
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[0] == False:
				button0.config(state="disabled")
				button0.config(text="O")
				marcados[0] = True
				marcacoes_computador[0] = True
			elif marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
				marcacoes_computador[8] = True
		#diagonal secundária
		elif (minhas_marcacoes[2] == False and minhas_marcacoes[4] == False and minhas_marcacoes[6] == False) and (marcados[2] == False or marcados[4] == False or marcados[6] == False):
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
				marcacoes_computador[2] = True
			elif marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
				marcacoes_computador[6] = True
		#primeira linha
		elif (minhas_marcacoes[0] == False and minhas_marcacoes[1] == False and minhas_marcacoes[2] == False) and (marcados[0] == False or marcados[1] == False or marcados[2] == False):
			if marcados[1] == False:
				button1.config(state="disabled")
				button1.config(text="O")
				marcados[1] = True
				marcacoes_computador[1] = True
			elif marcados[0] == False:
				button0.config(state="disabled")
				button0.config(text="O")
				marcados[0] = True
				marcacoes_computador[0] = True
			elif marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
				marcacoes_computador[2] = True
		#terceira linha
		elif (minhas_marcacoes[6] == False and minhas_marcacoes[7] == False and minhas_marcacoes[8] == False) and (marcados[6] == False or marcados[7] == False or marcados[8] == False):
			if marcados[7] == False:
				button7.config(state="disabled")
				button7.config(text="O")
				marcados[7] = True
				marcacoes_computador[7] = True
			elif marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
				marcacoes_computador[6] = True
			elif marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
				marcacoes_computador[8] = True
		#primeira coluna
		elif (minhas_marcacoes[0] == False and minhas_marcacoes[3] == False and minhas_marcacoes[6] == False) and (marcados[0] == False or marcados[3] == False or marcados[6] == False):
			if marcados[3] == False:
				button3.config(state="disabled")
				button3.config(text="O")
				marcados[3] = True
				marcacoes_computador[3] = True
			elif marcados[0] == False:
				button0.config(state="disabled")
				button0.config(text="O")
				marcados[0] = True
				marcacoes_computador[0] = True
			elif marcados[6] == False:
				button6.config(state="disabled")
				button6.config(text="O")
				marcados[6] = True
				marcacoes_computador[6] = True
		#segunda coluna
		elif (minhas_marcacoes[1] == False and minhas_marcacoes[4] == False and minhas_marcacoes[7] == False) and (marcados[1] == False or marcados[4] == False or marcados[7] == False):
			if marcados[4] == False:
				button4.config(state="disabled")
				button4.config(text="O")
				marcados[4] = True
				marcacoes_computador[4] = True
			elif marcados[1] == False:
				button1.config(state="disabled")
				button1.config(text="O")
				marcados[1] = True
				marcacoes_computador[1] = True
			elif marcados[7] == False:
				button7.config(state="disabled")
				button7.config(text="O")
				marcados[7] = True
				marcacoes_computador[7] = True
		#terceira coluna
		elif (minhas_marcacoes[2] == False and minhas_marcacoes[5] == False and minhas_marcacoes[8] == False) and (marcados[2] == False or marcados[5] == False or marcados[8] == False):
			if marcados[5] == False:
				button5.config(state="disabled")
				button5.config(text="O")
				marcados[5] = True
				marcacoes_computador[5] = True
			elif marcados[2] == False:
				button2.config(state="disabled")
				button2.config(text="O")
				marcados[2] = True
				marcacoes_computador[2] = True
			elif marcados[8] == False:
				button8.config(state="disabled")
				button8.config(text="O")
				marcados[8] = True
				marcacoes_computador[8] = True

		elif marcados[5] == False:
			button5.config(state="disabled")
			button5.config(text="O")
			marcados[5] = True
			marcacoes_computador[5] = True
		elif marcados[3] == False:
			button3.config(state="disabled")
			button3.config(text="O")
			marcados[3] = True
			marcacoes_computador[3] = True
		elif marcados[1] == False:
			button1.config(state="disabled")
			button1.config(text="O")
			marcados[1] = True
			marcacoes_computador[1] = True
		elif marcados[2] == False:
			button2.config(state="disabled")
			button2.config(text="O")
			marcados[2] = True
			marcacoes_computador[2] = True
		elif marcados[0] == False:
			button0.config(state="disabled")
			button0.config(text="O")
			marcados[0] = True
			marcacoes_computador[0] = True
		elif marcados[4] == False:
			button4.config(state="disabled")
			button4.config(text="O")
			marcados[4] = True
			marcacoes_computador[4] = True
		elif marcados[6] == False:
			button6.config(state="disabled")
			button6.config(text="O")
			marcados[6] = True
			marcacoes_computador[6] = True
		elif marcados[7] == False:
			button7.config(state="disabled")
			button7.config(text="O")
			marcados[7] = True
			marcacoes_computador[7] = True
		elif marcados[8] == False:
			button8.config(state="disabled")
			button8.config(text="O")
			marcados[8] = True
			marcacoes_computador[8] = True

	def checar_empate():
		global vitoria_jogador
		global vitoria_computador
		global marcados
		print(vitoria_computador)
		print(vitoria_jogador)
		print(marcados)
		if vitoria_computador == False and vitoria_jogador == False and marcados == [True, True, True, True, True, True, True, True, True]:
			janela_resultado("Empate!")

	def checar_vitoria_jogador():
		global vitoria_jogador
		global minhas_marcacoes
		if minhas_marcacoes[0] == True and minhas_marcacoes[1] == True and minhas_marcacoes[2] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[3] == True and minhas_marcacoes[4] == True and minhas_marcacoes[5] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[6] == True and minhas_marcacoes[7] == True and minhas_marcacoes[8] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[3] == True and minhas_marcacoes[6] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[1] == True and minhas_marcacoes[4] == True and minhas_marcacoes[7] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[5] == True and minhas_marcacoes[8] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[0] == True and minhas_marcacoes[4] == True and minhas_marcacoes[8] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")
		if minhas_marcacoes[2] == True and minhas_marcacoes[4] == True and minhas_marcacoes[6] == True:
			vitoria_jogador = True
			janela_resultado("Você ganhou!")

	def checar_vitoria_computador():
		global vitoria_computador
		global marcacoes_computador
		if marcacoes_computador[0] == True and marcacoes_computador[1] == True and marcacoes_computador[2] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[3] == True and marcacoes_computador[4] == True and marcacoes_computador[5] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[6] == True and marcacoes_computador[7] == True and marcacoes_computador[8] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[0] == True and marcacoes_computador[3] == True and marcacoes_computador[6] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[1] == True and marcacoes_computador[4] == True and marcacoes_computador[7] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[2] == True and marcacoes_computador[5] == True and marcacoes_computador[8] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[0] == True and marcacoes_computador[4] == True and marcacoes_computador[8] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")
		if marcacoes_computador[2] == True and marcacoes_computador[4] == True and marcacoes_computador[6] == True:
			vitoria_computador = True
			janela_resultado("Você perdeu!")

	def novo_jogo(root):
		global marcados
		global minhas_marcacoes
		global marcacoes_computador
		global vitoria_computador
		global vitoria_jogador
		root.quit()
		root.destroy()
		vitoria_computador = False
		vitoria_jogador = False
		marcados = [False, False, False, False, False, False, False, False, False]
		minhas_marcacoes = [False, False, False, False, False, False, False, False, False]
		marcacoes_computador = [False, False, False, False, False, False, False, False, False]
		jogo_da_velha()

	def janela_resultado(texto):
		def novo_jogo(root2):
			global marcados
			global minhas_marcacoes
			global marcacoes_computador
			global vitoria_computador
			global vitoria_jogador
			root2.quit()
			root2.destroy()
			vitoria_computador = False
			vitoria_jogador = False
			marcados = [False, False, False, False, False, False, False, False, False]
			minhas_marcacoes = [False, False, False, False, False, False, False, False, False]
			marcacoes_computador = [False, False, False, False, False, False, False, False, False]
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
		global marcacoes_computador
		button0.config(state="disabled")
		button0.config(text="X")
		marcados[0] = True
		minhas_marcacoes[0] = True

		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao1():
		global marcados
		global minhas_marcacoes
		button1.config(state="disabled")
		button1.config(text="X")
		marcados[1] = True
		minhas_marcacoes[1] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao2():
		global marcados
		global minhas_marcacoes
		button2.config(state="disabled")
		button2.config(text="X")
		marcados[2] = True
		minhas_marcacoes[2] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao3():
		global marcados
		global minhas_marcacoes
		button3.config(state="disabled")
		button3.config(text="X")
		marcados[3] = True
		minhas_marcacoes[3] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao4():
		global marcados
		global minhas_marcacoes
		button4.config(state="disabled")
		button4.config(text="X")
		marcados[4] = True
		minhas_marcacoes[4] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao5():
		global marcados
		global minhas_marcacoes
		button5.config(state="disabled")
		button5.config(text="X")
		marcados[5] = True
		minhas_marcacoes[5] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao6():
		global marcados
		global minhas_marcacoes
		button6.config(state="disabled")
		button6.config(text="X")
		marcados[6] = True
		minhas_marcacoes[6] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao7():
		global marcados
		global minhas_marcacoes
		button7.config(state="disabled")
		button7.config(text="X")
		marcados[7] = True
		minhas_marcacoes[7] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	def marcar_botao8():
		global marcados
		global minhas_marcacoes
		button8.config(state="disabled")
		button8.config(text="X")
		marcados[8] = True
		minhas_marcacoes[8] = True
		movimento_computador()
		checar_vitoria_jogador()
		checar_vitoria_computador()
		checar_empate()

	root = tk.Tk()
	root.geometry("800x640")
	menu_bar = tk.Menu(root)
	menu_menu = tk.Menu(menu_bar, tearoff=0)
	menu_menu.add_command(label="Novo Jogo", command=lambda: novo_jogo(root))
	menu_menu.add_command(label="sair", command=sair)
	menu_sobre = tk.Menu(menu_bar, tearoff=0)
	menu_sobre.add_command(label="sair", command=sair)
	menu_bar.add_cascade(label="Menu", menu=menu_menu)
	menu_bar.add_cascade(label="Sobre", menu=menu_sobre)
	root.config(menu=menu_bar)

	button0 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao0)
	button0.grid(column=1, row=1)

	button1 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao1)
	button1.grid(column=2, row=1)

	button2 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao2)
	button2.grid(column=3, row=1)

	button3 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao3)
	button3.grid(column=1, row=2)

	button4 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao4)
	button4.grid(column=2, row=2)

	button5 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao5)
	button5.grid(column=3, row=2)

	button6 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao6)
	button6.grid(column=1, row=3)

	button7 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao7)
	button7.grid(column=2, row=3)

	button8 = tk.Button(root, text="", width=20, height=10, font=("arial", 16), command=marcar_botao8)
	button8.grid(column=3, row=3)

	root.mainloop()
if __name__ == "__main__":
	jogo_da_velha()
