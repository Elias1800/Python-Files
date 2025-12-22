# Manipulação de arquivos de texto

# Ler o arquivo

# with open("arquivo.txt","r",encoding='utf-8') as f:
#    print(f.read())

# Exibir linha por linha 
# with open("arquivo.txt","r",encoding='utf-8') as f:
#    print(f.read())

# texto = input("Qual termo deseja procurar no arquivo? ")
# contador_linhas = 1
# contador = 1

# try:

#    with open("C:\\Python-Files\\Manipulacao_de_arquivos\\arquivo.txt","r",encoding='utf-8') as f:

#       for linha in f: 
#          linha = linha.rstrip()

#          if texto in linha:
#             print(f"O termo foi encontrado na linha {contador}!")
#             print(linha,'\n')

#          else:
#             contador_linhas =+ 1
         
#          contador =+ 1

#       if contador_linhas == contador:
#          print("Termo não encontrado!")

# except Exception as erro:
#    print(erro)

# Esrever em arquivos de texto
try:
   with open("C:\\Python-Files\\Manipulacao_de_arquivos\\arquivo.txt","a",encoding='utf-8') as f:
      f.write("\nAdicionando novas linhas com append\n" \
      "Continuação da linha anterior 1")

except Exception as erro:
   print(erro)

