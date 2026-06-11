# Declaração de Classe
class Lima:
    def __init__(self, nome =  "", idade = 0): # Método Construtor
        # Atributtos de Instancias
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto e tem {self.idade} anos de idade."

#Declaração de Objetos
g1 = Lima("Alexandre", 30)
g1.aniversario()
print(g1.mensagem())

g2 = Lima("Arrascaeta", 33)
g2.aniversario()
print(g2.mensagem())

g3 = Lima()
print(g3.mensagem())
