class RPN_calc:
    def __init__(self):
        self.stack = []
        self.op = 0
        self.start()

    def start(self):
        print("digite os números e as operações. Digite 'c' para retirar o último número da pilha\n"
              "Digite cl para zerar tudo. Digite 'n' quando terminar")
        while True:
            self.op = input("digite um número ou operação: ")
            if self.op.isnumeric():
                self.stack.append(self.op)
                print(self.stack)
            #self.op == "+" or self.op == "-" or self.op == "/" or self.op == "**":
            if self.op == "n":
                print("programa finalizado")
                break
            if self.op == "cl":
                self.stack.clear()
                print(self.stack)
            if self.op == "c":
                self.stack.pop()
                print(self.stack)
            if len(self.stack) <= 1:
                print("Número de entradas insuficiente")
                continue
            if self.op == "*":
                total = 1
                for num in self.stack:
                    total *= float(num)
                self.stack.clear()
                self.stack.append(total)
                print(f"resultado parcial: {self.stack[0]}")
            if self.op == "+":
                total = 0
                for num in self.stack:
                    total += float(num)
                self.stack.clear()
                self.stack.append(total)
                print(f"resultado parcial: {self.stack[0]}")
            if self.op == "-":
                total = 0
                for num in self.stack:
                    total -= float(num)
                self.stack.clear()
                self.stack.append(total)
                print(f"resultado parcial: {self.stack[0]}")
            if self.op == "/":
                total = float(self.stack[0])
                for num in self.stack[1:]:
                    if float(num) != 0:
                        total /= float(num)
                        self.stack.clear()
                        self.stack.append(total)
                        print(self.stack)
                    else:
                        print("divisão por 0 não é permitido. Último número retirado")
                        self.stack.pop()
                        print(self.stack)
            if self.op == "**":
                total = float(self.stack[0])
                for num in self.stack[1:]:
                    total **= float(num)
                self.stack.clear()
                self.stack.append(total)


calc = RPN_calc()


