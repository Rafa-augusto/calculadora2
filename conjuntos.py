from time import sleep
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
<<<<<<< HEAD
            break
=======
            break
>>>>>>> c1cb4710a799c5f9252a043644855d2243f35ebc
