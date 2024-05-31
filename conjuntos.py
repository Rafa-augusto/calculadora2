from time import sleep
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
            inter.append(A)
            inter.append(B)
            



conjuntos_numericos()
