import time
import random
#Exemplos de matrizes para teste. em que a "matriz15" tem 15 pontos de entrega
    # matriz15 =  [[0,0,'F',0,'B',0],['K',0,'A','H',0,0],[0,'C',0,'I','G',0],['N',0,'D',0,'J',0],['R',0,0,'E',0,0],[0,'L',0,'O',0,'M']]
    # matriz14 =  [[0,0,'F',0,'B',0],['K',0,'A','H',0,0],[0,'C',0,'I','G',0],['N',0,'D',0,'J',0],['R',0,0,'E',0,0],[0,'L',0,0,0,'M']]
    # matriz13 =  [[0,0,'F',0,'B',0],['K',0,'A','H',0,0],[0,'C',0,'I','G',0],[0,0,'D',0,'J',0],['R',0,0,'E',0,0],[0,'L',0,0,0,'M']]
    # matriz12 =  [[0,0,'F',0,'B',0],['K',0,'A','H',0,0],[0,'C',0,'I','G',0],[0,0,'D',0,'J',0],['R',0,0,'E',0,0],[0,'L',0,0,0,0]]
    # matriz11 =  [[0,0,'F',0,'B',0],['K',0,'A','H',0,0],[0,'C',0,'I','G',0],[0,0,'D',0,'J',0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
    # matriz10 =  [[0,0,'F',0,'B',0],[0,0,'A','H',0,0],[0,'C',0,'I','G',0],[0,0,'D',0,'J',0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
    # matriz9 =  [[0,0,'F',0,'B',0],[0,0,'A','H',0,0],[0,'C',0,'I','G',0],[0,0,'D',0,0,0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
    # matriz8 =  [[0,0,'F',0,'B',0],[0,0,'A','H',0,0],[0,'C',0,0,'G',0],[0,0,'D',0,0,0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
    # matriz7 =  [[0,0,'F',0,'B',0],[0,0,'A',0,0,0],[0,'C',0,0,'G',0],[0,0,'D',0,0,0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
    # matriz6 =  [[0,0,'F',0,'B',0],[0,0,'A',0,0,0],[0,'C',0,0,0,0],[0,0,'D',0,0,0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
matriz5 =  [[0,0,0,0,'B',0],[0,0,'A',0,0,0],[0,'C',0,0,0,0],[0,0,'D',0,0,0],['R',0,0,'E',0,0],[0,0,0,0,0,0]]
    # matriz4 =  [[0,0,0,0,'B',0],[0,0,'A',0,0,0],[0,'C',0,0,0,0],[0,0,'D',0,0,0],['R',0,0,0,0,0],[0,0,0,0,0,0]]
    # matriz3 =  [[0,0,0,0,'B',0],[0,0,'A',0,0,0],[0,'C',0,0,0,0],[0,0,0,0,0,0],['R',0,0,0,0,0],[0,0,0,0,0,0]]
    # matriz2 =  [[0,0,0,0,'B',0],[0,0,'A',0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],['R',0,0,0,0,0],[0,0,0,0,0,0]]
    # matriz1 =  [[0,0,0,0,0,0],[0,0,'A',0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],['R',0,0,0,0,0],[0,0,0,0,0,0]]
    # matrizr =  [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],['R',0,0,0,0,0],[0,0,0,0,0,0]]
    # matriz0 =  [[0,0,0,0,0,0],[0,0,'A',0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

inicio = time.time()
pontoR = [-1,-1]

#aqui será colocada a matriz a ser analisada
matriz = matriz5

def gerar_pop_inicial(lista,pop_size):
    individuos = []
    individuos.append(lista)
    if len(lista) < 5: 
        if len(lista) == 3:
            pop_size = 6
        else: pop_size = 24
    i = 1
    while i < pop_size:
        new = lista.copy()
        random.shuffle(new)
        if new not in individuos:
            i += 1
            individuos.append(new)
    return individuos
    
def distancia(ponto1,ponto2): return ((ponto1[1] - ponto2[1]) ** 2 + (ponto1[2] - ponto2[2]) ** 2) ** 0.5

def avalia_indi(indi,restaurante):

    r1 = distancia(indi[0],restaurante)
    rn = distancia(restaurante,indi[-1])
    distancia_total = r1 + rn
    for i in range(len(indi)-1):
        distancia_total += distancia(indi[i],indi[i+1])
    return distancia_total

def avalia_pop(pop,restaurante):
    apts = []
    distancias = []
    max = 0
    for individuo in pop:
        apt = avalia_indi(individuo,restaurante)
        distancias.append(apt)
        if apt > max: max = apt
        apts.append(apt)
    for i, apt in enumerate(apts):
        apts[i] = max - apt
    return apts, distancias

def torneio(data,APTS):

    pop = data['pop']
    apts = APTS
    num_ind = len(pop)
    pais_indexes = []

    for i in range(num_ind):
        pai1_index = random.randint(0,num_ind-1)
        pai2_index = random.randint(0,num_ind-1)
        if apts[pai1_index] > apts[pai2_index]: pais_indexes.append(pai1_index)
        else: pais_indexes.append(pai2_index)
    return pais_indexes

def crossover(pai_indexes,data,APTS,cross):

    num_pais = len(pai_indexes)
    filhos = []
    num_fil = 0

    while num_fil < num_pais:
        p1 = data['pop'][random.randint(0,num_pais-1)]
        p2 = data['pop'][random.randint(0,num_pais-1)]

        if random.random() <= cross:
            filho1 = PMX(p1,p2)
            filho2 = PMX(p1,p2)
            filhos.append(filho1)
            filhos.append(filho2)
            num_fil+=2

    if num_fil > num_pais: filhos.pop()
    return filhos

def PMX(p1,p2):

    divisao = random.randint(1,len(p1[0])-2)

    filho = p1.copy()
    filho = filho[:divisao]

    for gene in p2:
        if gene not in filho: filho.append(gene)

    return filho

def mutacao(pop,mut):
    
    for filho in pop:
        if random.random() <= mut:
            gene_mut = random.randint(0,len(pop[0])-2)
            pop[gene_mut], pop[gene_mut+1] = pop[gene_mut+1], pop[gene_mut], 

def acha_r(matriz):
    list = [-1,-1]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (matriz[i][j]) != (0):
                if str(matriz[i][j]) == 'R': 
                    list = ['R',i,j]
    return list

def cria_lista(matriz):
    list = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (matriz[i][j]) != (0):
                if str(matriz[i][j]) != 'R': list.append([matriz[i][j],i,j])
    return list

def main(lista,restaurante):

    cross = 0.7
    mut = 0.01
    ger = 30000
    pop_size = 70

    convergencia = True
    ok = False

    pop = gerar_pop_inicial(lista,pop_size)
    apts, distancias = avalia_pop(pop,restaurante)
    
    data = { "pop": pop, "apts": apts }
    APTS = apts

    geracao = 0
    
    the_best1 = 0
    the_best2 = 0
    the_best3 = 0

    #while geracao < ger:
    while ok == False:
        pop_sel = torneio(data,APTS)
        fil_sel = crossover(pop_sel,data,APTS,cross)
        
        mutacao(fil_sel,mut)
        apts, distancias = avalia_pop(fil_sel,restaurante)

        data['pop'] = pop
        
        if convergencia == True:
            if geracao % 3 == 0: the_best1 = APTS.index(max(APTS))
            if geracao % 3 == 1: the_best1 = APTS.index(max(APTS))
            if geracao % 3 == 2: the_best3 = APTS.index(max(APTS))

            if the_best1 == the_best2 and the_best2 == the_best3:
                ok = True
                break

        geracao += 1

    i_melhor = the_best1
    return (data['pop'][i_melhor],distancias[i_melhor])


lista = cria_lista(matriz)
pontoR = acha_r(matriz)
melhor = []

if pontoR[1] == -1: print("Essa matriz não tem um ponto R")
elif lista == []: print("Essa matriz não tem pontos de entrega")
else: 
    if len(lista) > 2: melhor = main(lista,pontoR) 
    else: melhor = lista
print(melhor)
fim = time.time()
print(fim - inicio, "segundos")