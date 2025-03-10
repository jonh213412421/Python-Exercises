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

print(sys.argv)

if len(sys.argv) == 0:
    print("funções:\n "
          "encrypt (mensagem)/(caso não tenha mensagem, ele abrirá um dialog para carregar um documento de texto) -> criptografa mensagem\n"
          "decrypt (mensagem)/(caso não tenha mensagem, ele abrirá um dialog para carregar um arquivo criptografado) -> descriptografa mensagem\n"
          "Importante: delete os arquivos originais assim que possível. Guarde as chaves em um lugar seguro.\n")
if sys.argv[1] == "encrypt" and len(sys.argv) == 2:
    caminho_arquivo = filedialog.askopenfile(title="escolha o caminho do arquivo")
    with open(caminho_arquivo, "r") as f:
        texto = f.read()
        f.close()
    encrypt.encrypt(texto)
if sys.argv[1] == "encrypt" and len(sys.argv) > 2:
    texto = ''.join(sys.argv[2:])
    encrypt.encrypt(texto)
if sys.argv[1] == "encrypt" and len(sys.argv) < 2:
    print("Erro! Por favor, revise os argumentos.")

if sys.argv[1] == "decrypt" and len(sys.argv) == 2:
    caminho_chave = filedialog.askopenfile(title="escolha o caminho da chave").name
    caminho_cifra = filedialog.askopenfile(title="escolha o caminho da cifra").name
    decrypt.decrypt(caminho_chave, caminho_cifra)
if sys.argv[1] == "decrypt" and len(sys.argv) != 2:
    print("Erro! Por favor, revise os argumentos.")
