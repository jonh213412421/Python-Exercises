import sys
import os
import decrypt
import encrypt
from tkinter import filedialog

if not os.path.exists(os.path.join(os.getcwd(), "chave")):
    os.mkdir(os.path.join(os.getcwd(), "chave"))
if not os.path.exists(os.path.join(os.getcwd(), "cifra")):
    os.mkdir(os.path.join(os.getcwd(), "cifra"))
if not os.path.exists(os.path.join(os.getcwd(), "mensagens")):
    os.mkdir(os.path.join(os.getcwd(), "mensagens"))

print(len(sys.argv))
if len(sys.argv) == 0:
    print("funções:\n "
          "encrypt (mensagem)/(caso não tenha mensagem, ele abrirá um dialog para carregar um documento de texto) -> criptografa mensagem\n"
          "decrypt (mensagem)/(caso não tenha mensagem, ele abrirá um dialog para carregar um arquivo criptografado) -> descriptografa mensagem\n")
if sys.argv[1] == "encrypt" and len(sys.argv) == 2:
    caminho_arquivo = filedialog.askopenfile()
    with open(caminho_arquivo, "r") as f:
        texto = f.read()
    encrypt.encrypt(texto)
if sys.argv[1] == "encrypt" and len(sys.argv) > 2:
    texto = ''.join(sys.argv[2:])
    encrypt.encrypt(texto)
