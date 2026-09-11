'''
Repetições
Whhile(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito -> Quando um códigonão tem fim'''

contador = 0

while contador <= 100:
    contador +=1

    if contador == 6:
        print("Não vou mostrar o 6.")
        continue

    if contador >= 10 and contador <= 27:
            print(f"Não vou mostrar o {contador}")
            continue
    if contador == 40:
         break
    print(contador)

print("Acabou")