from math import sqrt

#Tratamento de Erros ou Exceçõoes em Python

def div():

    print("\nStart Programa: Divisão\n")

    while True:
        try: 
            n1 = float(input("Insira o primeiro valor: "))
            n2 = float(input("Insira o segundo valor: "))
            r = n1/n2

        except ZeroDivisionError:
            print(f"Erro: Não é possivel fazer divisões por zero!\n")

        except ValueError:
            print("Erro: Valor não identificado, tente novamente!\n")

        else:
            print(f"A divisão de {n1} por {n2} é igual a: {r:.2f}")
            break

        finally:
            print("\nPrograma Finalizado!")
        
#Tratamento usando raise

def Raiz_Quadrada():

    print("\nStart Programa: Raiz Quadrada\n")
    while True:
        n = float(input("Digite um número positivo: "))
        try:
            if n < 0:
                raise ArithmeticError

        except ArithmeticError:
            print("Você digitou um valor negativo, tente novamente!")  
        else: 
            print(f"A raiz quadrada de {n} é {sqrt(n):.2f}\n")
            break
        finally:
            print("Programa Finalizado!")



if __name__ == "__main__":
        div()
        Raiz_Quadrada()
