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

if len(sys.argv) == 0:
    print("funções:\n "
          "encrypt (mensagem)/(caso não tenha mensagem, ele abrirá um dialog para carregar um documento de texto) -> criptografa mensagem\n"
          "decrypt (mensagem)/(caso não tenha mensagem, ele abrirá um dialog para carregar um arquivo criptografado) -> descriptografa mensagem\n")
if sys.argv[1] == "encrypt" and len(sys.argv) == 2:
    caminho_arquivo = filedialog.askopenfile(title="escolha o caminho do arquivo")
    with open(caminho_arquivo, "r") as f:
        texto = f.read()
        f.close()
    encrypt.encrypt(texto)
if sys.argv[1] == "encrypt" and len(sys.argv) > 2:
    texto = ''.join(sys.argv[2:])
    encrypt.encrypt(texto)
    
if sys.argv[1] == "decrypt_a" and len(sys.argv) == 2:
    caminho_chave = filedialog.askopenfile(title="escolha o caminho da chave")
    caminho_cifra = filedialog.askopenfile(title="escolha o caminho da cifra")
    with open(caminho_chave, "r") as f:
        chave = f.read()
        f.close()
    with open(caminho_cifra, "r") as f:
        cifra = f.read()
        f.close()
    decrypt.decrypt(chave, cifra)
if sys.argv[1] == "decrypt_s" and len(sys.argv) == 2:
    chave = sys.argv[2]
    texto = sys.argv[3]
    encrypt.encrypt(texto)
if sys.argv[1] == "decrypt_s" and len(sys.argv) > 2:
    print("argumentos incorretos")
