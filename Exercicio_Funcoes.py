# Função de boas-vindas
def boas_vindas(nome):
    print(f"Olá {nome}, seja bem vindo!")

nome = "Elias"
boas_vindas(nome)

# Soma e média
def soma_media(a,b,c):
    soma = a + b + c
    media = soma / 3
    return soma, media

s, m = soma_media(4, 7, 9)
print(f"Soma = {s}, Média = {m:.2f}")

# Verificar par ou ímpar
def par_ou_impar(num):
    if num % 2 == 0 :
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")

num = 5
par_ou_impar(num)

# Calcular idade
def calculo_idade(y1,y2):
    return y1 - y2

y1,y2 = 2004,2025
calculo_idade(y1,y2)

# Maior número da lista

def maior_valor(a):
    print(max(a))

lista = [2,3,4,12,5,24]
maior_valor(lista)