import os
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
    xor = ''.join('1' if palavra[i] != chave_binario[i] else '0' for i in range(len(palavra)))
    while not gravado:
        try:
            print(i)
            if os.path.exists(os.path.join(dir_chave, f"chave{i}.enc")):
                i = i + 1
            else:
                with open(os.path.join(dir_chave, f"chave{i}.enc"), "wb") as f:
                    f.write(chave_binario.encode())
                    f.close()
                with open(os.path.join(dir_cifra, f"cifra{i}.enc"), "wb") as f:
                    f.write(xor.encode())
                    f.close()
                gravado = True
            print("Processo concluído com êxito!")
        except:
            print("Erro!")
    print(f"chave: {chave_binario}")
    print(f"cifra: {xor}")
    
