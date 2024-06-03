from math import sqrt
from numpy import linspace
import matplotlib.pyplot as plt
from time import sleep

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
<<<<<<< HEAD
            break
=======
            break
>>>>>>> c1cb4710a799c5f9252a043644855d2243f35ebc
