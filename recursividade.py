import os
#Função Fatorial
def fatorial(n):
    if n == 0 or n == 1: 
        print(f"1 = ", end="")
        return 1
    else:
        print(f"{n} * ",end="")
        return  n * fatorial(n - 1) 

#Sequencia Fibonacci 
def seq_fibonacci(n):

    seq=[]
 
    for  i in range(n+1):
        seq.append(fibonacci(i))
    
    return seq

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if __name__ == '__main__':
    
    while True:

        print("\n================")
        print("1. Fatorial")
        print("2. Fibonacci")
        print("0. sair")
        print("================\n")

        op = int(input("Escolha uma opção: "))
        print('')
        validador = True

        match op:

            case 1:

                while validador:  

                    try:
                        entrada = int(input("Insira um valor para fatoração: "))

                    except ValueError:
                        print("Erro: Digite apenas números inteiros.\n")

                    except RecursionError:
                        print("Erro: Valor fornecido é muito grande.\n")
                    
                    if entrada < 0:
                        print("Erro: número negativo não possui fatorial.\n")
                        continue

                    else:
                        print(fatorial(entrada),"\n")

                        while True:

                            ft_nv = input("Digite S para sair ou N para fazer outra fatoração: ")

                            if ft_nv.lower() == 's': 
                                os.system('cls')
                                validador = False
                                break
                            elif ft_nv.lower() == 'n':
                                os.system('cls')
                                break
                            else :
                                print("Erro: Opção invalida!\n")
            case 0:
                print("Programa finalizado!")
                break
               
    
