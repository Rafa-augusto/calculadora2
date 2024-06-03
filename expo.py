from numpy import linspace
import matplotlib.pyplot as plt
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
<<<<<<< HEAD
    grafico(a,b)
=======
    grafico(a,b)
>>>>>>> c1cb4710a799c5f9252a043644855d2243f35ebc
