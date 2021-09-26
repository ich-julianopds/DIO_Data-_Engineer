class Calculadora:
    def __init__(self, num_1, num_2):
        self.valor_a = num_1
        self.valor_b = num_2


    def soma(self):
        return self.valor_a + self.valor_b


    def subtracao(self):
        return self.valor_a - self.valor_b


    def multiplicacao(self):
        return self.valor_a * self.valor_b


    def divisao(self):
        return self.valor_a / self.valor_b


calculadora = calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
