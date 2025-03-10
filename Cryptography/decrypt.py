import os

def decrypt(caminho_cifra: str, caminho_chave: str) -> None:

    mensagem = ""
    dir_mensagem = os.path.join(os.getcwd(), "mensagens")
    with open(caminho_chave, "r") as f:
        chave2 = f.read()
        f.close()
    with open(caminho_cifra, "r") as f:
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
            if os.path.exists(os.path.join(dir_mensagem, f"mensagem{i}.txt")):
                i = i + 1
            else:
                with open(os.path.join(dir_mensagem, f"mensagem{i}.txt"), "w") as f:
                    f.write(str(mensagem))
                    f.close()
                gravado = True
        except:
            print("Erro!")
