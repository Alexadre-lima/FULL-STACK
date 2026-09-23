'''
Repetições
Whhile(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito -> Quando um códigonão tem fim'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        coluna += 1
        print(linha, coluna)

    linha += 1
    

print("Acabou")