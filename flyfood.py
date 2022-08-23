#FLYFOOD

import time
inicio = time.time()
matriz = [[0,0,0,0,'D'],[0,0,'C',0,0],[0,'A','R','B',0],[0,0,0,0,0],[0,0,0,0,0]]

list = []

iniciox = int(-1)

def linha(x,matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(matriz[i][j]) == x: 
             return i

def coluna(x,matriz):

   for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(matriz[i][j]) == x: 
             return j
            
def menorCaminho(permutas,inicioX,inicioY,matriz):
    menorx = 0
    for j in range(len(permutas)):
        rota = 0
        for i in range(0,len(permutas[j])):
         if i == 0 or  i == len(permutas[j])-1: 
            rota += abs(inicioX - linha(permutas[j][i],matriz)) + abs(inicioY - coluna(permutas[j][i],matriz))
         else: 
            rota += abs(linha(permutas[j][i+1],matriz)-linha(permutas[j][i],matriz)) + abs(coluna(permutas[j][i+1],matriz) - coluna(permutas[j][i],matriz))
        if j == 0 : menor = rota  
        elif rota < menor: 
            menor = rota
            menorx = j
        else: menor = menor
    return permutas[menorx]

def permutacao(lista):
    
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return [lista]

    lista_auxiliar = [] 

    for indice in range(len(lista)):
        chave = lista[indice] 
        lista_sem_chave = lista[:indice] + lista[indice + 1:] 
        for p in permutacao(lista_sem_chave):
            lista_auxiliar.append([chave] + p)
    return lista_auxiliar 

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (matriz[i][j]) != (0):
            if str(matriz[i][j]) == 'R': 
                inicioX = i
                inicioY = j
            else: list.append(matriz[i][j])

if inicioX == -1: print("Essa matriz não tem um ponto R")
elif list == []: print("Essa matriz não tem pontos de entrega")
else:
    permutas = permutacao(list)
    if permutas == [list]: print(permutas)
    else: 
        print(menorCaminho(permutas,inicioX,inicioY,matriz))
fim = time.time()
print(fim - inicio)