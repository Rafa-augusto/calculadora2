import numpy as np
import matplotlib.pyplot as mp
def conjuntos_numericos():
    A = []
    B = []
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
    while True:
        print(f"A = {A} B = {B}\n-----Selecione uma opção-----\n1. Verificar se A é subconjunto de B\n2. A união com B\n3. A intersecção com B\n4. Diferença entre A e B")
        "\n"
        opcao = int(input("Sua opção: "))
conjuntos_numericos()