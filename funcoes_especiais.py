# Função Lambda
quadrado = lambda n: n**2

for i in range(21):
    print(quadrado(i))

# Função map()
# Sintaxe = map(função,interável)

num = [21,32,54,6546,4,14,25,3]

dobro = list(map(lambda x: x*2, num))
print(dobro)

palavra = ['Hoje','é','terça','e','amanhã','será','quarta!']
maiusculas = list(map(lambda s: s.upper(), palavra))
print(maiusculas)

# Função filter()
# Sintaxe = filter(função, sequência) 

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) 
num_impares = list(filter(lambda x: x % 2 != 0, numeros))  
print(num_impares)

# Função reduce()
# Sintaxe = reduce(função, sequência, valor_inicial)

from functools import reduce

numeros_1 = [1,2,3,4,5]
total = reduce(lambda x, y: x + y, numeros_1)
print(total)