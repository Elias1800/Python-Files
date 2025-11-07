import sys
import os

# Função para calculo das raizes
def raizes(a,b,c):
    delta = (b**2 - 4*a*c)
    x1 = (-b + delta**(1/2) / (2*a))
    x2 = (-b - delta**(1/2) / (2*a))

    print(f"\n O valor de x1: {x1:.2f}")
    print(f"\n O valor de x2: {x2:.2f}")

if __name__ == '__main__':
    print(f"Calcular as raízes de uma equação de 2º grau\n")
    print(f"Equação no formato ax² + bx + c = 0\n")

    while True:
        try:
            a = float(input("Insira o valor de a: "))
            b = float(input("Insira o valor de b: "))
            c = float(input("Insira o valor de c: "))

        except ValueError:
            print(f"\nErro: Insira apenas números!\n")
        else:
            raizes(a,b,c)
           
        while True:
            Continue = input(f"Digite 'S' para sair ou 'N' para novo calculo: ")
            if (Continue.lower()) == 's':
                print("\nPrograma Finalizado! :D\n") 
                sys.exit()
            elif(Continue.lower() == 'n'):
                os.system('cls')
                break       
            else:
                print("Erro: Entrada Invalida")

    