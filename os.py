import os

# Programa  para renomer  varios arquivos dentro de uma pasta

os.chdir('C:\\Python-Files\\Teste os')

padrao_arquivo = input("\nNovo nome dos arquivos: ")

for contador, arquivo in enumerate(os.listdir()):
    
    if os.path.isfile(arquivo):

        nome_arquivo, extencao_arquivo = os.path.splitext(arquivo)
        nome_arquivo = padrao_arquivo +' '+str(contador+1)

        nome_novo =  f'{nome_arquivo}{extencao_arquivo}'
        os.rename(arquivo,nome_novo)

print("Arquivos renomeados!\n")
