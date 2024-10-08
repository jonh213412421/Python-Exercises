#basic class structure
class test:
    #init
    def __init__(self):
        self.oi = "oi"
    #interaction with init
    def hello(self):
        print(self.oi)
    #more complex usage
    def hello_name(self, name):
        print(f"hello, {name}")

#calling class
name = "Henry"
teste = test()
teste.hello()
teste.hello_name(name)

#calculator implementation
class op:
    def __init__(self):
        op = input("qual é a operação? ")
        self.op = op
    def numbers(self):
        self.numbers = []
        while True:
            num = input("digite um número: ")
            if num == '':
                pass
            else:
                if num.lower() == "fim":
                    break
                self.numbers.append(num)
                print(self.numbers)
        if self.op == "*":
            resultado = float(self.numbers[0])
            for numero in self.numbers[1:]:
                    resultado *= float(numero)
                    print(resultado)
        if self.op == "**":
            resultado = float(self.numbers[0])
            for numero in self.numbers[1:]:
                    resultado **= float(numero)
                    print(resultado)
        if self.op == "/":
            resultado = float(self.numbers[0])
            for numero in self.numbers[1:]:
                    resultado /= float(numero)
                    print(resultado)
        if self.op == "+":
            resultado = float(self.numbers[0])
            for numero in self.numbers[1:]:
                    resultado += float(numero)
                    print(resultado)
        if self.op == "-":
            resultado = float(self.numbers[0])
            for numero in self.numbers[1:]:
                    resultado -= float(numero)
                    print(resultado)

#calling calculator
if __name__ == "__main__":
    op = op()
    op.numbers()
