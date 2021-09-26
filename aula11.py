
lista = [1,10]
try:
    divisao = 10 / 1
    numero = lista[3]
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um indice inválido na lista')
#except:   Poderia colocar como erro genérico, e neste caso é só colocar o except
#    print('Erro')
