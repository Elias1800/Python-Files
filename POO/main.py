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
    def set_cor_veiculo(self,cor):
        self.__cor = cor

# Heranças
class Carro(Veiculo):
    #Classe
    def __init__(self, nome, marca, fabricante, ano):
        super().__init__(nome, marca, fabricante, ano)

    # Metodos
    def carro_andando(self):
        print(f"O carro está andando!")

# Objetos 

Carro = Carro('Camaro','toyota','jep',1800)
Carro.set_cor_veiculo('Preto')
Carro.carro_andando()
print(Carro.ver_dados())