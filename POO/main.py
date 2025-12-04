# Classes
class Veiculo:
    # Atributos
    def __init__(self, nome, marca, fabricante, ano):
        self.__nome = nome
        self.__marca = marca
        self.__fabricante = fabricante
        self.__ano = ano
        self.__cor = None

    #getter 
    def ver_dados(self):
        return  f"Nome: {self.__nome}\nMarca: {self.__marca}\nFabricante: {self.__fabricante}\nAno: {self.__ano}\nCor: {self.__cor}"
    
    #setter
    def cor_veiculo(self,cor):
        self.__cor = cor



#Objetos
Veiculo1 = Veiculo("Fiat Tourino","Jeep","Fiat",2000)
print(Veiculo1.ver_dados(),"\n")
Veiculo1.cor_veiculo("Amarelo")
print(Veiculo1.ver_dados())