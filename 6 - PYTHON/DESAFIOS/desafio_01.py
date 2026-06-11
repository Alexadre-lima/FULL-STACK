#IMPRIMIR UMA LISTA DE NOMES

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

'''for i in range(len(nomes)):
    print(nomes[i], idades[i])
    '''
for nome, idade in zip(nomes, idades):
    print(nome, idade)