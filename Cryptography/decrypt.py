import os
#change
import random

def decrypt(chave: str, cifra: str) -> None:
    mensagem = ""
    dir_chave = os.path.join(os.getcwd(), "chave")
    dir_cifra = os.path.join(os.getcwd(), "cifra")
    dir_mensagem = os.path.join(os.getcwd(), "mensagens")
    with open(os.path.join(dir_chave, f"{chave}.enc"), "r") as f:
        chave2 = f.read()
        f.close()
    with open(os.path.join(dir_cifra, f"{cifra}.enc"), "r") as f:
        cifra = f.read()
        f.close()
    xor = ''.join(str(int(chave2[i]) ^ int(cifra[i])) for i in range(len(chave2)))
    for i in range(0, len(xor), 8):
        byte = int(xor[i:i + 8], 2)
        char = chr(byte)
        print(char)
        mensagem += char
    i = 0
    gravado = False
    while not gravado:
        try:
            print(i)
            if os.path.exists(os.path.join(dir_mensagem, f"mensagem{i}.enc")):
                i = i + 1
            else:
                with open(os.path.join(dir_chave, f"chave{i}.enc"), "w") as f:
                    f.write(str(mensagem))
                    f.close()
                with open(os.path.join(dir_cifra, f"cifra{i}.enc"), "w") as f:
                    f.write(str(xor))
                    f.close()
                gravado = True
        except:
            print("Erro!")

#decrypt("chave1", "cifra1")
