def potencias(M, N, V, f):
    count, erro = 0, 1
    z = [0 for i in range(0, N)]
    erro_aux = [0 for i in range(0, N)]
    print("Iteração\tAutovalor\t\tErro Relativo")
    while(1):
        #print("\n---> Iteração K = {}".format(count+1))
        for i in range(0, N):
            for j in range(0, N):
                z[i] += M[i][j]*V[j]
        #print("\nVetor (Xk) = {}".format(V))
        zmax = max([abs(i) for i in z])
        
        for i, v in enumerate(z):
            z[i] = v/zmax
        soma = sum(z)
        
        for i, v in enumerate(z):   # normalizando
            z[i] = v/soma
        
        #print("Vetor (Rk) = {}".format(z))
        
        for i in range(0, N):
            erro_aux[i] = abs(abs(z[i])-abs(V[i]))
        erro = max(erro_aux)
        
        #print("\nLk = {}".format(zmax))
        f.write("{}\t{}".format(zmax, erro))
        print("{}\t\t{}\t{}".format(count, zmax, erro))
        V = z[:]
        count += 1
        if erro < 5e-5 or count == 25:
            break
        
    return zmax, z
    
def calcula_m(A, S, M, N):
    for i in range(0, N):
        for j in range(0, N):
            M[i][j] = (0.85*A[i][j] + 0.15*S)
            print("M[{}][{}] = {}".format(i+1, j+1, M[i][j]))
    
def main():
    f = open("exercico2.txt", "w+")
    for i in range(0, 4):
        if i == 0:
            A = [[0, 0, 1, 1/2], 
                 [1/3, 0, 0, 0],
                 [1/3, 1/2, 0, 1/2], 
                 [1/3, 1/2, 0, 0]]
            N = 4
            print("------------------------------------ A ------------------------------------")
        elif i == 1:
            A = [[0, 1, 0, 0, 0], 
                 [1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1/2], 
                 [0, 0, 1, 0, 1/2], 
                 [0, 0, 0, 0, 0]]
            N = 5
            print("\n------------------------------------ B ------------------------------------")
        elif i == 2:
            A = [[0, 0, 1/2, 1/2, 0], 
                 [1/3, 0, 0, 0, 0], 
                 [1/3, 1/2, 0, 1/2, 1],
                 [1/3, 1/2, 0, 0, 0],
                 [0, 0, 1/2, 0, 0]]
            N = 5
            print("\n------------------------------------ C ------------------------------------")
        elif i == 3:
            A = [[0, 0, 1/2, 1/2, 0, 1/5], 
                 [1/3, 0, 0, 0, 0, 1/5], 
                 [1/3, 1/2, 0, 1/2, 1, 1/5],
                 [1/3, 1/2, 0, 0, 0, 1/5],
                 [0, 0, 1/2, 0, 0, 1/5],
                 [0, 0, 0, 0, 0, 1/5]]
            N = 6
            print("\n------------------------------------ D ------------------------------------")
        
        M = [[0 for j in range(0, N)] for i in range(0, N)]
        S = 1/N
        V = [1/N for i in range(0, N)]
        
        print("\nMatriz M atual --> M = 0.85A + 0.15S\n")
        calcula_m(A, S, M, N)
        
        print("\n\nVetor V atual: --> vetor y0 com todos os componentes iguais a 1/n  \n")
        for i in range(0, N):
            print("V[{}] = {}".format(i, V[i]))
        
        print("\n\nMetodo da Potencia para a M: \n")
        autovalor, autovetor = potencias(M, N, V, f)
        print("\nO Autovalor: {}".format(autovalor))
        print("O Autovetor: {}".format(autovetor))
        print("SOMA PORRA: {}".format(sum(autovetor)))
    f.close()
        
main()
    
    