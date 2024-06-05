from time import sleep
from numpy import linspace
import matplotlib.pyplot as plt
from math import sqrt

def f_delta_e_raízes(a,b,c):
    delta = b**2 - (4*a*c)
    
    if delta==0:
        raizX1 = (-b)/(2*a) #Obs do Leonardo: Aqui não importa se fizer a raíz de delta, pois é 0, então somar ou diminuir não faz diferença, então só tirei todo o calculo de detla
        return a,b,c,raizX1
    elif delta>0:
        raizX1 = (-b + sqrt(delta))/(2*a)
        raizX2 = (-b - sqrt(delta))/(2*a)
        return a,b,c,raizX1, raizX2
    elif delta<0: #Não existe, mas tem que ter, por que em testes anteriores não funcionava sem ter os calculos
        raizReal= -b/(2*a)
        raizComplexa = sqrt(-delta)/(2*a)
        raizX1 = (raizReal, raizComplexa)
        raizX2 = (raizReal, -raizComplexa)
        return a,b,c,raizX1, raizX2
    return delta
def funcao_f_calculo(x,a,b,c):
    f = a*(x**2) + b*x + c
    return f
def f_vertíce(a,b,c):
    Xv = -b/(2*a)
    Yv = funcao_f_calculo(Xv,a,b,c)
    tipo="mínimo" if a > 0 else "máximo"
    return Xv,Yv, tipo
def f_gráfico(a,b,c):
    x = linspace(-10,10,400)
    y = funcao_f_calculo(x,a,b,c,)
    plt.plot(x, y, label= f"f(x) = {a}x² + {b}x + {c}")
    plt.title("Função do Segundo Grau: ax² + bx + c")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
def f_formatacao_das_raizes(raizX1, raizX2):
    def formatacao(raiz):
        if isinstance (raiz, tuple):
            raizReal, raizComplexa = raiz
            if raizReal == 0:
                return f"{raizComplexa:.2f}i"
            elif raizComplexa == 0:
                return f"{raizReal:.2f}"
            else:
                sinal = "+" if raizComplexa > 0 else "-"
                return f"{raizReal:.2f} {sinal} {abs(raizComplexa):.2f}i"
        else:
            return f"{raiz:.2f}"
    return formatacao(raizX1), formatacao(raizX2)
def finalização_de_tudo():
    print("Função de Segundo Grau: f(x) = ax² + bx + c")
    a=float(input("Digite o coeficiente 'a' da equação: "))
    b=float(input("Digite o coeficiente 'b' da equação: "))
    c=float(input("Digite o coeficiente 'c' da equação: "))
    while True:
        sleep(0.5)
        print(end="\n")
        print("-----|Menu|-----")
        print("1. Realizar calculo das raízes\n2. Calcular 'x' da função\n3. Calcular Vértice\n4. Gerar Gráfico da Fução f(x)\n5. Sair")
        op=int(input("Digite o número da sua escolha: "))
        print(end="\n")
        if op>5 or op<1:
            print("Opção inválida!")
        elif op==1:
            a, b, c, raizX1, raizX2 = f_delta_e_raízes(a,b,c) #Obs do Leonardo: Calculo das Raízes
            x1_formatada,x2_formata = f_formatacao_das_raizes(raizX1,raizX2)
            print(f"As raizes da função são: {x1_formatada} e {x2_formata}")
        elif op==2:
            x=float(input("Insira o valor 'x' para a função f(x): ")) #Obs do Leonardo: Subistituição do x por número escolhido pelo usuário
            resposta= funcao_f_calculo(x,a,b,c)
            print(f"f({x}) = {resposta}")
        elif op==3:
            Xv, Yv, tipo = f_vertíce(a,b,c)
            print(f"Os vértices da função são: ({Xv}, {Yv}), sendo um ponto {tipo} ")
        elif op==4:
            f_gráfico(a,b,c)
        else:
            print("Saindo...")
            sleep(1)
            break

def gerar_matriz_Multi(linhas, colunas):
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
                    print(end="\n")
                    print("A matriz possui determinante.")   
            else:
                print("A raiz não possui determinante.") 
        elif opcao == 2:
            print(end="\n")
            linhasmulti = int(input("Defina o número de linhas para a multiplicação de matrizes: "))
            colunasmulti = int(input("Agora o número de colunas: "))
            matrizmulti = gerar_matriz_Multi(linhasmulti,colunasmulti)
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
                    print(matriz[i])
                print("x")
                for i in range(linhasmulti):
                    print(matrizmulti[i])
                print("=")
                for i in range(linhas):
                    print(matrizmultiplicada[i])
            else:
                print("A multiplicação é impossível")
        elif opcao == 3:
            matriztrans = []
            for i in range(colunas):
                linhaT = []
                for i in range(linhas):
                    linhaT.append(0)
                matriztrans.append(linhaT)
            for i in range(colunas):
                for j in range(linhas):
                    matriztrans[i][j] = matriz[j][i]
            for i in range(colunas):
                print(matriztrans[i])
            print(end="\n")
        elif opcao == 4:
            print("saindo...")
            sleep(1)
            break

def coeficientes():
    cont=0
    while cont==0:
        a = float(input("Insira o coeficiente 'a', sem que seja 0: "))
        b = float(input("Insira o coeficiente 'b', sem que seja 0, e diferente de 1: "))
        if a and b !=0 and b>1:
            cont+=1
            return a,b
        else:
            print("Algum número é inválido, por favor, tente novamente!")
        continue
def calculo_da_funcao(x,a,b):
    f = a*(b**x)
    return f
def verificação_da_expressao(a,b):
    if b>1 and a>1:
        return("A função é crescente")
    elif b<1 or a<1:
        return("A função é decrescente")
    else:
        return("A função é decrescente")
def grafico(a,b):
    x = linspace(-10,10,400)
    y = calculo_da_funcao(x,a,b)
    plt.plot(x, y, label= f"f(x)= {a}({b}*x)")
    plt.title("Função Exponencial: f(x) = ab^x")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
def fim():
    a,b=coeficientes()
    cres_decres= verificação_da_expressao(a,b)
    print(f"A funçãoa é: {cres_decres}")
    x=float(input("Insira o valor 'x' para descobrir o resultado: "))
    conta=calculo_da_funcao(x,a,b)
    print(f"f({x})= {conta}")

def conjuntos_numericos():
    A = []
    B = []
    tempo1 = 0
    tempo2 = 0
    while True:
        a = int(input("Selecione o número de itens para o conjunto A: "))
        b = int(input("Agora o número de itens para B: "))
        if a<0 or b<0:
            print("\"ERRO\" número inválido")
            continue
        else:
            break
    for i in range(a):
        x = int(input("Digite o número para o subconjunto A: "))
        A.append(x) 
    for i in range(b):
        y = int(input("Digite o número para o subconjunto B: "))
        B.append(y)   
    while tempo1<len(A):
                if A.count(A[tempo1])>1:
                    A.remove(A[tempo1])
                tempo1+=1
    while tempo2<len(B):
                if B.count(B[tempo2])>1:
                    B.remove(B[tempo2])
                tempo2+=1
    while True:
        sleep(0.5)
        print(end="\n")
        print(f"A = {sorted(A)} B = {sorted(B)}\n-----Selecione uma opção-----\n1. Verificar se A é subconjunto próprio de B\n2. A união com B\n3. A intersecção com B\n4. Diferença entre A e B\n5.Sair")
        print(end="\n")
        opcao = int(input("Sua opção: "))
        if opcao<1 or opcao>5:
            print("ERRO")
            continue
        elif opcao == 1:
            if len(A) != len(B):
                print("B não é subconjunto próprio de A.")
                continue
            else:
                answer = []
                for i in range(len(A)):
                    if A[i] != B[i]:
                        answer.append(1)
                    else:
                        answer.append(0)
                if sum(answer) == 0:
                    print("A é subconjunto próprio de B")
                    continue
                else:
                    print("A não é um subconjunto próprio de B")
                    continue
        elif opcao == 2:
            Uniao = []
            Uniao.extend(A)
            Uniao.extend(B)
            cont = 0
            while cont<len(Uniao):
                if Uniao.count(Uniao[cont])>1:
                    Uniao.remove(Uniao[cont])
                cont+=1
            print(f"A união entre A e B é igual a {sorted(Uniao)}")
        elif opcao == 3:
            inter = []
            inter.extend(A)
            inter.extend(B)
            cont1 = 0
            cont2 = 0
            print(sorted(inter))
            while cont1<len(inter):   
                if inter.count(inter[cont1])==1:
                    inter.remove(inter[cont1])
                else:
                    cont1+=1
            while cont2<len(inter):
                if inter.count(inter[cont2])>1:
                    inter.remove(inter[cont2])
                cont2+=1
            print(f"A intersecção entre A e B é igual a {sorted(inter)}")
        elif opcao == 4:
            dif = []
            dif.extend(A)
            dif.extend(B)
            dif.sort()
            print(dif)
            cont = 0
            cont1 = 0
            while cont<len(dif):
                if dif.count(dif[cont])>1:
                    dif.remove(dif[cont])
                cont+=1
            while cont1<len(dif):
                for i in range(len(B)):
                    if dif[cont1] == B[i]:
                        dif.remove(dif[cont1])
                cont1+=1
            print(f"A diferença entre os conjuntos A e B é {sorted(dif)}")
        elif opcao == 5:
            print("Saindo..")
            sleep(1)
            break
        




def menu():
    while True:
        print("--Menu principal--\n1.Conjunto numéricos\n2.Funções de Segundo Grau\n3.Funções exponenciais\n4.Matrizes\n5.Sair")
        opcao = int(input("Selecione uma opção: "))
        if opcao<1 or opcao>5:
            print("ERRO")
            continue
        elif opcao==1:
            conjuntos_numericos()
            continue
        elif opcao==2:
            finalização_de_tudo()
            continue
        elif opcao==3:
            fim()
            continue
        elif opcao==4:
            linhas = int(input("Digite o número de linhas para a matriz: "))
            colunas = int(input("Digite o número de colunas para a matriz: "))
            gerar_matriz(linhas,colunas)
            continue
        else:
            print("Saindo...")
            break
menu()
