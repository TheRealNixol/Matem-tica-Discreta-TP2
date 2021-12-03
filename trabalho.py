import numpy as np
import os
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import csv

#Métodos para os Exercicios

#método para limpar a consola ao voltar ao menu
def clearConsole():
    #utilizamos o metodo system da libraria OS para correr o comando Clear.
    os.system("clear")

def exercicio1():
    #indico ao python que quero utilizar uma variavel global ao programa que se encontra fora do método
    #esta variavel menu_active servirá para que possa navegar de volta para o menu sempre que desejar, dentro do exercicio 1
    global menu_active 
    active = True
    while active:
        try:
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
            #Inicialização e Requesito dos valores V0 e G
            print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 1__________________\u001b[0m\u001b[0m\u001b[0m\n")
            print("y(t) = v0*t - 1/2*g*t**2")
            v0 = float(input("\nIntroduza o valor da velocidade inicial (m/s): ".encode('utf8').decode('iso-8859-1')))
            g = float(input("\nIntroduza o valor da acelaração gravitica (m/s**2): ".encode('utf8').decode('iso-8859-1')))
            #De seguida o código tenta requisitar um valor valido de tempo ao utilizador
            try:
                t = float(input("\nIntroduza o valor do tempo (s): ".encode('utf8').decode('iso-8859-1')))
                #se o valor de tempo for menor ou igual a 0, o código irá devolver uma mensagem de erro
                if t >= 0:
                    #caso contrario o programa calcula o valor de y utilizando os valores indicados pelo utilizador
                    y = (v0 * t) - (1/2 * g * t**2)
                    #Por fim arredondo o resulta de Y em 2 casas decimais e retorno o resultado ao utilizador
                    y = round(y, 2)
                    print("---------\u001b[32mResultado\u001b[0m----------\n")
                    print(" y(t) = %s (m)" % y)
                    print("\n----------------------------")
                else:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\n O valor de tempo deve ser positivo ou igual a 0.\n".encode('utf8').decode('iso-8859-1'))
            except ValueError:
                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                print("\nFoi atribuido um valor não permitido de tempo, por favor volte novamente.\n".encode('utf8').decode('iso-8859-1'))
            
            #crio um ciclo para perguntar ao utilizar se deseja dar nova entrada ao exercico 1 ou voltar ao menu 
            perg1_respondida = False
            while perg1_respondida == False:
                try:
                    print("\n______________________________________________________________________________________________\n")
                    perg1_resposta = int(input("Deseja continuar no Exercicio 1 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                    if perg1_resposta == 1:
                        perg1_respondida = True
                        active = True
                    elif perg1_resposta == 2:
                        perg1_respondida = True
                        active = False
                        menu_active = True
                        #ao retornar, limpamos a consola ao utilizar o metodo descrito em cima clearConsole() 
                        clearConsole()
                    else:
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                except ValueError:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
        except ValueError:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nFoi atribuido um valor não permito, por favor introduza novamente os valores ! (Exemplo: 2.4)\n".encode('utf8').decode('iso-8859-1'))

def exercicio2():
    global menu_active
    active = True
    while active:
        try:
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
            print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 2__________________\u001b[0m\u001b[0m\u001b[0m\n")
            print("y(t) = v0*t - 1/2*g*t**2")
            #começamos por armazenar os valores indicados pelo utilizador para a velocidade inicial, força gravitica e o intervalo de tempo. ti = tempo inicial do intervalo & tf = tempo final do intervalo 
            v0 = float(input("\nIntroduza o valor da velocidade inicial: ".encode('utf8').decode('iso-8859-1')))
            g = float(input("Introduza o valor da acelaração gravitica: ".encode('utf8').decode('iso-8859-1')))
            ti = float(input("Introduza o tempo inicial (s):".encode('utf8').decode('iso-8859-1')))
            tf = float(input("Introduza o tempo final (s):".encode('utf8').decode('iso-8859-1')))
            # verificamos se o tempo final é superior ao tempo inical do intervalo. Caso contrario é devolvida uma mensagem de erro.
            if tf > ti:
                #depois de validadas as entradas, começamos por utilizar o metodo linspace para criar um intervalo de tempo(matriz de valores) entre os valores inseridos pelo utilizador
                t = np.linspace(ti,tf)
                #de seguida podemos utilizar a matriz de t para calcular o valor de y respetivo aos varios pontos de tempo da matriz t durante a queda do objeto
                y = (v0 * t) - (1/2 * g * t**2)
                #utilizamos metodos da biblioteca Matplotlib para criar o titulo, legenda e rotulos dos eixos para o grafico.
                plt.title("Grafico da queda-livre".encode('utf8').decode('iso-8859-1')) 
                plt.xlabel("Valor do tempo da queda (s)".encode('utf8').decode('iso-8859-1'))
                plt.ylabel("Valor da posicao do objeto (m)".encode('utf8').decode('iso-8859-1'))
                plt.legend(("y(t) = v0*t - 1/2*g*t**2"))
                #por fim fazemos o plot dos valores relacionados t e y e representamos o gráfico ao utilizador
                ax = plt.plot(t,y)
                plt.show()
                print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
                #volto ao menu com a mesma forma logica explicada no exercicio 1
                #crio um ciclo para perguntar ao utilizar se deseja ou não fazer a conversão e se quer manter-se no exercicio 2 com uma nova entrada ou voltar ao menu 
                perg1_respondida = False
                while perg1_respondida == False:
                    try:
                        print("\n______________________________________________________________________________________________\n")
                        perg1_resposta = int(input("Deseja continuar no Exercicio 2 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                        if perg1_resposta == 1:
                            perg1_respondida = True
                            active = True
                        elif perg1_resposta == 2:
                            perg1_respondida = True
                            active = False
                            menu_active = True
                            clearConsole()
                        else:
                            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                            print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                    except ValueError:
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
            else:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\nTempo final não pode ser inferior ao tempo inicial !\n".encode('utf8').decode('iso-8859-1'))
        except ValueError:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nAlgo correu mal do código do exercicio. Volte a tentar mais tarde!\n".encode('utf8').decode('iso-8859-1'))
             
def exercicio3():
    global menu_active
    active = True
    while active:
        try:
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
            print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 3__________________\u001b[0m\u001b[0m\u001b[0m\n")
            # declaramos uma variavel ficheiro para obter uma referencia ao ficheiro data.csv do diretorio
            ficheiro = open('data.csv')
            # utilizamos o metodo reader da biblioteca CSV para ler o ficheiro referenciado pela variavel ficheiro
            leitor = csv.reader(ficheiro)
            # criamos 3 matrizes vazias onde os valores serão inseridos
            x = []
            y = []
            z = []
            #com um ciclo for, percorremos as linhas e inserimos as 3 primeiras posições de valores em linha nas matrizes declaradas em cima
            #ao inserir os valores nas respetivas matrizes, estes saõ transformados em floats pois, de outra forna seriam interpretados como strings
            for row in leitor:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
                    z.append(float(row[2]))
            #criamos uma figura atraves do metodo figure da biblioteca Matplotlib
            fig = plt.figure()
            #indicamos que se trata de uma representação 3D
            ax = plt.axes(projection="3d")
            #sobre em representação 3D, utilizamos o metodo plot_trisurf para criar um relacionamento a ser representado entre as matrizes de X,Y e Z 
            ax.plot_trisurf(x,y,z)
            #por fim inserior rotulos para uma melhor interpretação do grafico e apresentamos o mesmo ao utilizador
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')

            plt.show()

            #volto ao menu com a mesma forma logica explicada no exercicio 1
            respondido = False
            while respondido == False:
                try:
                    perg1_resposta = int(input("Introduza [1] para voltar ao menu de navegação! ".encode('utf8').decode('iso-8859-1')))
                    respondido = True
                    if perg1_resposta == 1:
                        menu_active = True
                        active = False
                        clearConsole()
                    else:
                        respondido = False
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\nNão foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                except ValueError:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\nNão foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))


        except ValueError:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nFoi atribuido um valor não permito, por favor volte novamente a introduzir todos valores para a lista (os valores devem ser inteiros e positivos).\n".encode('utf8').decode('iso-8859-1'))
    
#Opener com informação relevante á aplicação
print("""\u001b[34m
 _______  _______ _________ _______  _______  _______ __________________ _______  _______    ______  _________ _______  _______  _______  _______ _________ _______ 
(       )(  ___  )\__   __/(  ____ \(       )(  ___  )\__   __/\__   __/(  ____ \(  ___  )  (  __  \ \__   __/(  ____ \(  ____ \(  ____ )(  ____ \\__   __/(  ___  )
| () () || (   ) |   ) (   | (    \/| () () || (   ) |   ) (      ) (   | (    \/| (   ) |  | (  \  )   ) (   | (    \/| (    \/| (    )|| (    \/   ) (   | (   ) |
| || || || (___) |   | |   | (__    | || || || (___) |   | |      | |   | |      | (___) |  | |   ) |   | |   | (_____ | |      | (____)|| (__       | |   | (___) |
| |(_)| ||  ___  |   | |   |  __)   | |(_)| ||  ___  |   | |      | |   | |      |  ___  |  | |   | |   | |   (_____  )| |      |     __)|  __)      | |   |  ___  |
| |   | || (   ) |   | |   | (      | |   | || (   ) |   | |      | |   | |      | (   ) |  | |   ) |   | |         ) || |      | (\ (   | (         | |   | (   ) |
| )   ( || )   ( |   | |   | (____/\| )   ( || )   ( |   | |   ___) (___| (____/\| )   ( |  | (__/  )___) (___/\____) || (____/\| ) \ \__| (____/\   | |   | )   ( |
|/     \||/     \|   )_(   (_______/|/     \||/     \|   )_(   \_______/(_______/|/     \|  (______/ \_______/\_______)(_______/|/   \__/(_______/   )_(   |/     \|
                                                                                                                                                                    
                                                                                                                                                                    \u001b[0m""")
print("\u001b[1m\u001b[4m   *** Bem Vindo ao trabalho desenvolvido no intuito da cadeira \n de Matemática Discreta do TIWM - Bruno Monteiro e João Almeida ***\n Por favor utilize o menu de selecção para navegar pela aplicação!\n\u001b[0m".encode('utf8').decode('iso-8859-1'))
print("\u001b[33m!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?\u001b[0m")
print("      Continuar[1]                  Sair[2]")
print("\u001b[33m!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?\n\u001b[0m")
resp = 0
while resp != 1 and resp != 2:
    #Fortalecer contra input que não se trate de um int (strings, especial characters, etc..)
    try:
        resp = int(input("Deseja continuar?   "))
        #Check if int as the value 1 or 2, otherwise same error message.
        if resp == 1:
            menu_active = True
        elif resp == 2:
            menu_active = False
            break
        else:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nNão foi introduzida uma opção disponivel, por favor tente novamente!\n".encode('utf8').decode('iso-8859-1'))
    except ValueError:
        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
        print("\nNão foi introduzida uma opção disponivel, por favor tente novamente!\n".encode('utf8').decode('iso-8859-1'))
    

#Menu da Aplicação

#criamos um dicionario com as opções do menu
menu = {}
menu['1']="Exercicio 1"
menu['2']="Exercicio 2"
menu['3']="Exercicio 3"
menu['4']="Exit"

#criamos um ciclo onde o menu corre infinitamente ate que o valor de menu_active seja falso
while menu_active:
    print("\n\u001b[36m///////////////// Menu de Navegação ///////////////////\n\u001b[0m".encode('utf8').decode('iso-8859-1'))
    options=menu.keys()
    #imprimo o dicionario com um ciclo for onde junto as keys com os seus respetivos valores numa so string impressa
    for entry in options:
        print("Opção[%s] - %s\n".encode('utf8').decode('iso-8859-1') % (entry,menu[entry]))
    #requer uma opção das listadas ao utilizador
    selection=input("Seleciona uma das opções: ".encode('utf8').decode('iso-8859-1'))
    #se for uma opção valida para os respetivos exercicios:
    #      1- Menu_active passa a false (para que o menu não seja constatemente aberto dentro dos exercicios)
    #      2- E executo um metodo do exercicio escolhido pelo utilizador 
    if selection =='1':
        menu_active = False
        exercicio1() 
    elif selection == '2':
        menu_active = False
        exercicio2()
    elif selection == '3':
        menu_active = False
        exercicio3()
    elif selection == '4':
        #se a opção for sair, então partimos o ciclo do menu, que terminara o programa 
        break
    #se for inserida uma opção que não seja permitida, será devolvido uma mensagem de erro que, como o menu_active continua a verdadeiro, retorna o utilizador ao menu 
    else:
        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
        print("\nNão foi introduzida uma opção disponivel, por favor tente novamente!\n".encode('utf8').decode('iso-8859-1'))
