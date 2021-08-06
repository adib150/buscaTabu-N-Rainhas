import random
import numpy as np

def tabuleiro(posicoesrainhas):
    n = len(posicoesrainhas)
    for linha in range(0,n):
        for coluna in range(0,n):
            if posicoesrainhas[coluna] == linha:
                print('R',end=" ")
            else:
                print ("|",end=" ")
        print()
 
def eval(posicoesrainhas):
    eval=0
    n= len(posicoesrainhas)
    for posicao1 in range(0,n):
        for posicao2 in range (posicao1+1,n):
            if posicoesrainhas[posicao1] == posicoesrainhas[posicao2]: #calcular eval de rainhas que se atacam na mesma linha
                eval=eval+1 #
                
    matrix = np.array([[0 for x in range(n)] for x in range(n)])
    for coluna in range(0,n):
        for linha in range(0,n):
            if posicoesrainhas[linha]==coluna:
                matrix[coluna][linha]=1
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])] #fazer as diagonais principais
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1)) #fazer as diagonais secundarias
    
    for diag in diags:
        vlr = np.sum(diag)-1
        while vlr>0:
            eval=eval+vlr #calcular eval das diagonais
            vlr=vlr-1
    return eval

def movimentar(posicoesrainhas,rainha,linha):
    posicoesrainhas[rainha]=linha
    return posicoesrainhas
    

def buscatabu(posicoesrainhas,listatabu):
    n= len(posicoesrainhas)
    melhoreval=99
    melhorestado=posicoesrainhas.copy()
    
    possiveleval=melhoreval
    possivelestado=posicoesrainhas.copy()
    
    rainhamovida=-1
    posicaoinicial=-1
    for rainha in range(0,n):
        if rainha not in listatabu: #nao visita colunas visitadas anteriormente
            posicaoinicial=possivelestado[rainha] 
            
            for linha in range(0,n):
                possivelestado[rainha] = linha
                possiveleval = eval(possivelestado)
                if melhoreval>possiveleval and possivelestado[rainha]!=posicoesrainhas[rainha]:
                     melhorestado=possivelestado.copy()
                     melhoreval=possiveleval
                     rainhamovida=rainha
            
            possivelestado[rainha]=posicaoinicial               

    #atualizar listatabu
    listatabu.insert(0,rainhamovida)
    listatabu.pop()
        
    print("Melhor eval da rodada:",melhoreval)
    print("Novas posicoes:",melhorestado)
    print("Nova ListaTabu: ",listatabu)
    tabuleiro(melhorestado)
    print()
    print()
    print()
    return melhorestado,listatabu

if __name__ == "__main__": 
    print("Seja bem vindo a busca tabu de n-rainhas.")
    n = int(input("Digite o tamaho do tabuleiro desejado: "))
    print ("Criando tabuleiro de tamanho:",n,"x",n)
    posicoesrainhas=np.random.randint(0,n,n) #Guarda posicoes das colunas das rainhas
    listatabu = [-1 for x in range(n-2)] #lista que nao pode ser visitada novamente
    print(listatabu)
    print ("initial solution (random):")
    print ("Posicoes:" , posicoesrainhas)
    tabuleiro(posicoesrainhas) #Printar o tabuleiro
    evaltabuleiroatual = eval(posicoesrainhas)
    print("Eval:",evaltabuleiroatual)
    
    while(evaltabuleiroatual>0):
        posicoesrainhas,listatabu = buscatabu(posicoesrainhas,listatabu)
        evaltabuleiroatual=eval(posicoesrainhas)
    