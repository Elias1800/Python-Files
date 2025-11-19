# Compreensões de listas
# Sintaxe básica: [expressão for item in iterável if condição]

# Exemplo 1: Criar uma lista com todas as vogais de uma frase

frase = "Um verdadeiro mestre é um eterno aprendiz."
vogais = ['a', 'e', 'i', 'o', 'u','á','é','í','ó','ú','à','è','ì','ò','ù','â','ê','î','ô','û','ã','õ']
lista_vogais = [i for i in frase if i in vogais]
print(f"Existem {len(lista_vogais)} vogais:")
print(lista_vogais)

# Exemplo 2 Criar uma lista com resultado de um calculo distributivo

distributiva = [x*y for x in [3,4,5] for y in [5,6,7]]
print(distributiva)

# Exemplo 3 Criar uma lista com números pares em um range
pares = [x for x in range(11) if x % 2 == 0]
print(pares)