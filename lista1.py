# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:27:48 2021

@author: splin
"""

###### Exercícios Lista 1
import numpy as np # Para o exercício 5


## Exercício 2
# Para implementar o exercício 2, é preciso realizar a implementação das funções
# propostas no exercício 1

def addxy(x, y):
    """
    Essa função realiza uma operação aritmética entre duas variáveis (soma).
    Input: dois valores: x e y.
    Output: printa uma frase que descreve a operação e o resultado. Como se trata
    de um print, guardar o resultado num objeto te dá um objeto de tipo NoneType.
    """
    print("The sum of {:d} and {:d} is: {:d}".format(x, y, x+y))

def mxy(x, y):
    """
    Essa função realiza uma operação aritmética entre duas variáveis (produto).
    Input: dois valores: x e y.
    Output: printa uma frase que descreve a operação e o resultado. Como se trata
    de um print, guardar o resultado num objeto te dá um objeto de tipo NoneType.
    """
    print("The product of {:d} and {:d} is: {:d}".format(x, y, x+y))

def dxy(x, y):
    """
    Essa função realiza uma operação aritmética entre duas variáveis (divisão).
    Input: dois valores: x e y.
    Output: printa uma frase que descreve a operação e o resultado. Como se trata
    de um print, guardar o resultado num objeto te dá um objeto de tipo NoneType.
    """
    print("The division of {:d} and {:d} is: {:d}".format(x, y, x+y))
    
addxy(1, 2)
mxy(1, 2)
dxy(1, 2)

# Definindo a função FEVAL
# Funciona como o pretendido
def feval(f, x, y):
    """
    Uma função que retorna o resultado de uma outra função considerando dois valores
    x e y.
    Input: uma função (f), e dois valores: x e y.
    Output: se o usuário passou uma função corretamente, a função é avaliada 
    com os valores x e y e seu resultado é retornado. Caso contrário, uma mensagem
    de aviso é printada.
    """
    if callable(f):
        return f(x, y) #  
    else:
        print("The user did not pass a function.")
feval(addxy, 1, 2)
feval(mxy, 1, 2)
feval(dxy, 1, 2)

## Exercício 5
# Essa rotina cria três objetos: uma lista com todos os elementos de uma matriz,
# um vetor com o de 5 elementos e outro vetor de 3 elementos. Tudo utilizando
# numpy para ganhos de velocidade.
# No arquivo de texto, a primeira linha deve ser, em orderm de linha e coluna, os elementos de A,
# depois os elementos de b e, por fim, os elementos de c. 


def string_cleaner(string):
    """
    Função auxiliar para a limpeza das linhas do arquivo.
    """
    return [int(x.strip()) for x in string.split(sep = ',')]


with open('C:\\Users\\splin\\Desktop\\Mestrado\\quarto\\listas\\input.txt') as f:
    lines = f.readlines()

A = string_cleaner(lines[0])
b = string_cleaner(lines[1])
c = string_cleaner(lines[2])

A = np.array(A)
A = A.reshape((5, 3))
b = np.array(b)
c = np.array(c)

print("Result from Ac:", np.dot(A, c)) 
print("Result from bA:", np.dot(b, A))


## Exercício 6
# Nesse caso, como precisamos medir a velocidade de operações, uma biblioteca específica é necessária
# No caso, para soma, multiplicação, divisão e exponenciação, eu utilizarei os operadores já imbutidos na linguagem
# para as funções trigonométricas, eu utilizarei as implementações do numpy
import os
import timeit
import pandas as pd

results = {}
operations = ["addition", "multiplication", "division", "exponentiation", "sine", "arc tangent"]

results[operations[0]] = timeit.timeit("a+b",setup = "a, b = 500, 600"  , number = 10000)
results[operations[1]] = timeit.timeit("a*b",setup = "a, b = 500, 600"  , number = 10000)
results[operations[2]] = timeit.timeit("a/b",setup = "a, b = 500, 600"  , number = 10000)
results[operations[3]] = timeit.timeit("a**b",setup = "a, b = 500, 600"  , number = 10000)
results[operations[4]] = timeit.timeit("np.sin(a)",setup = "import numpy as np; a = 500"  , number = 10000)
results[operations[5]] = timeit.timeit("np.arctan(a)",setup = "import numpy as np; a = 500"  , number = 10000)

# Queremos velocidades relativas. Vamos utilizar a velocidade mais lenta como base:
max_time = max(results.values())
relative_speed = []
for key in results.keys():
    relative_speed.append(results[key] / max_time)

# Como o exercício exige que os valores sejam comparados em diferentes plataformas, nós vamos
# pegar esses valores e exportá-los.

os.chdir("C:\\Users\\splin\\Desktop\\Mestrado\\quarto") # porque quero salvar em um local específico
data = pd.DataFrame({'operations':operations, 'values':results.values(), 'relative_values':relative_speed})
data.to_csv("data.csv")
