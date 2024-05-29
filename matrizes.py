from time import sleep

def gerar_matriz_Multi():
    linhas = int(input("Defina o número de linhas para a multiplicação de matrizes: "))
    colunas = int(input("Agora o número de colunas: "))
    matrizmulti = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            x = int(input("Digite um número para a linha: "))
            linha.append(x)
        matrizmulti.append(linha) 
    print(end="\n")
    return matrizmulti

def gerar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            x = int(input("Digite um número para a linha: "))
            linha.append(x)
        matriz.append(linha) 
    print(end="\n")
    for i in range(linhas):
        print(matriz[i])
    
    print(end="\n")
    while True:
        sleep(0.5)
        print(end="\n")
        print("--Escolha uma opção--\n1.Determinante(se possuír um)\n2.Multiplicação\n3.Transpor a matriz\n4.Sair")
        opcao = int(input("Sua opção: "))
        if opcao<1 or opcao>4:
            print("ERRO")
        elif opcao == 1:
            if linhas == colunas:
                if linhas == 1:
                    determinante = matriz[0][0]
                    print(end="\n")
                    print(f"A matriz possui determinante e ele é {determinante}.")                     
                elif linhas == 2:
                    determinante = (matriz[0][0]*matriz[1][1])-(matriz[1][0]*matriz[0][1])
                    print(end="\n")
                    print(f"A matriz possui determinante e ele é {determinante}.") 
                    continue
                elif linhas == 3:
                    determinante = (matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[0][1]*matriz[1][2]*matriz[2][0])+(matriz[0][2]*matriz[1][0]*matriz[2][1])-(matriz[2][0]*matriz[1][1]*matriz[0][2])-(matriz[2][1]*matriz[1][2]*matriz[0][0])-(matriz[2][2]*matriz[1][0]*matriz[0][1])
                    print(end="\n")
                    print(f"A matriz possui determinante e ele é {determinante}.")  
                else:
                    print("A matriz possui determinante.")   
            else:
                print("A raiz não possui determinante.") 
        elif opcao == 2:
            print(end="\n")
            matrizmulti = gerar_matriz_Multi()
            if len(matriz[0]) == len(matrizmulti):
                print("A multiplicação é possível")
                matrizmultiplicada = []
                for i in range(linhas):
                    multilinha = []
                    for j in range(len(matrizmulti[0])):
                        elemento = []
                        for h in range(len(matriz[0])):
                            calculo = matriz[i][h]*matrizmulti[h][j]
                            elemento.append(calculo)
                        multilinha.append(sum(elemento))
                    matrizmultiplicada.append(multilinha)
            
                for i in range(linhas):
                    print(matriz[i],"x",matrizmulti[i],"=",matrizmultiplicada[i])
            else:
                print("A multiplicação é impossível")
        elif opcao == 3:
            print(end="\n")

                
                            
                


gerar_matriz(2,3)