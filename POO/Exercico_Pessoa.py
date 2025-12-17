# Classe 
class Pessoa:
    # ATRIBUTOS
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    # Método
    def Apresentar(self):
        if self.idade >= 18:
            MaiorIdade = True
        else:
            MaiorIdade = False
        return f'Nome:{self.nome}\nIdade:{self.idade}\nMaior idade:{MaiorIdade}'
    

    