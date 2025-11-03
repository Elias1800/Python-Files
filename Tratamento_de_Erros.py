#Tratamento de Erros ou Exceçõoes em Python

print("\nInicio do Programa: Divisão\n")

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
        print("Programa Finalizado!")
    