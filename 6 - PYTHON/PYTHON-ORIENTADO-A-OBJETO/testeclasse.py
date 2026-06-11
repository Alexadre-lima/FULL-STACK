print(int.__doc__)

# DUNDER = Double Underline __
# Docstring

# Declaração de Classe
class Lima:

    '''
    Essa classe cria um gafanhoto, que é uma que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = gafanhoto(nome, idade)
    '''
    def __init__(self, nome =  "", idade = 0): # Método Construtor
        # Atributtos de Instancias
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto e tem {self.idade} anos de idade."
    
    def __str__(self): # Dunder Method
        return f"{self.nome} é um Gafanhoto e tem {self.idade} anos de idade."
      
#Declaração de Objetos
g1 = Lima("Alexandre", 30)
g1.aniversario()
print(g1.mensagem())

print(g1.__doc__) # Dunder attribute
print(g1)