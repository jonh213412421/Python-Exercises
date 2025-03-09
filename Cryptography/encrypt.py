import os
#change
import random

def encrypt(palavra: str) -> None:
    print(palavra)
    dir_chave = os.path.join(os.getcwd(), "chave")
    dir_cifra = os.path.join(os.getcwd(), "cifra")
    palavra = ''.join(format(ord(l), '08b') for l in palavra)
    print(f"binário original: {palavra}")
    chave = random.getrandbits(len(palavra))
    chave_binario = format(chave, f'0{len(palavra)}b')
    if not os.path.exists(dir_chave):
        os.mkdir(dir_chave)
    if not os.path.exists(dir_cifra):
        os.mkdir(dir_cifra)
    gravado = False
    i = 0
    xor = ''.join(str(int(palavra[i]) ^ int(chave_binario[i])) for i in range(len(palavra)))
    while not gravado:
        try:
            print(i)
            if os.path.exists(os.path.join(dir_chave, f"chave{i}.enc")):
                i = i + 1
            else:
                with open(os.path.join(dir_chave, f"chave{i}.enc"), "w") as f:
                    f.write(str(chave_binario))
                    f.close()
                with open(os.path.join(dir_cifra, f"cifra{i}.enc"), "w") as f:
                    f.write(str(xor))
                    f.close()
                gravado = True
        except:
            print("Erro!")
    print(f"chave: {chave_binario}")
    print(f"cifra: {xor}")


#encrypt("teste")
