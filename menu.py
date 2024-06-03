import conjuntos as cj
import segundograu as sg
import expo as ex
import matrizes as mz
def menu():
    print("--Menu principal--\n1.Conjunto numéricos\n2.Funções de Segundo Grau\n3.Funções exponenciais\n4.Matrizes\n5.Sair")
    opcao = int(input("Selecione uma opção: "))
    while True:
        if opcao<1 or opcao>5:
            print("ERRO")
            continue
        elif opcao==1:
            cj.conjuntos_numericos()
        elif opcao==2:
            sg.finalização_de_tudo()
        elif opcao==3:
            ex.fim()
        elif opcao==4:
            linhas = int(input("Digite o número de linhas para a matriz: "))
            colunas = int(input("Digite o número de colunas para a matriz: "))
            mz.gerar_matriz(linhas,colunas)
        else:
            print("Saindo...")
            break
menu()