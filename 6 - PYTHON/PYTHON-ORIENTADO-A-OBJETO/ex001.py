# Declaração de Classe
class Lima:
    def __init__(self): # Método Construtor
        # Atributtos de Instancias
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto e tem {self.idade} anos de idade."

#Declaração de Objetos
g1 = Lima()
g1.nome = "Alexandre"
g1.idade = 29
g1.aniversario()
print(g1.mensagem())

g2 = Lima()
g2.nome = "Arrascaeta"
g2.idade = 32
print(g2.mensagem())