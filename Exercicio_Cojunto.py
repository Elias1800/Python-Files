#Remover duplicatas de uma Lista

numeros = [1,2,3,4,4,5,6,7,8]

print(list(set(numeros)))

# Encontrar elementos comuns entre dois cojuntos

a = {1,2,3,4,5,6,7,8}
b = {1,5,6,7,9,12,23,45,123}

print(a & b)

#Verificar se um elemento está presente

frutas = {'Pera','Abacate','Maça','Uva'}

fruta = input("Insira um nome de uma fruta: ")
              
if fruta in frutas:
    print(f"{fruta} está no cojunto de frutas.")
else:
    print(f"{fruta} não está no cojunto das frutas.")

# Diferença entre conjuntos

A = {"python", "java", "c++", "go"}
B = {"java", "c#", "python"}

print(A-B)

#União e atualização

cores = {"vermelho", "azul"}
novas = {"verde", "amarelo"}

novas.add("branco")
novas.add("preto")
novas.add("bege")
novas.add("ciano")

print(cores.union(novas))