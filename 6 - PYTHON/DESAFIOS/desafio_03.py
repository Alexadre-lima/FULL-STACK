# Composição (Relalação forte / Vida ou morte)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f"endereço de {self.cidade}/{self.estado} foi apagado")

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def adicionar_endereco(self, cidade, estado):
        novo_endereco = Endereco(cidade, estado)
        self.enderecos.append(novo_endereco)

cliente_alexandre = Cliente("Alexandre")

cliente_alexandre.adicionar_endereco("Aracaju", "SE")
cliente_alexandre.adicionar_endereco("Tobias barreto", "SE")

print("FIM DO PROGRAMA, os endereço foram apagados")