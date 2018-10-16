#Instruções de jogo
def begin():
    print('\nBem vindo(s) ao nosso jogo da velha! O jogo é bem simples, primeiro, os jogadores escolherão qual sinal irão usar(x/o).\nPosteriormente, irão intercalar as rodadas informando com números as posições que querem jogar conforme o tabuleiro:\n\n _1_|_2_|_3_\n _4_|_5_|_6_\n _7_|_8_|_9_\n')
    input("Pressione ENTER para avançar ")

#Escolha de cada símbolo
jogador1 = ()
def player(jogador1):
    print('\n')
    valid = False
    while valid == False:
        jogador1 = input('Jogador 1, com qual símbolo deseja jogar?(x ou o): ').upper()
        if jogador1 == "X" or jogador1 == "O":
            if jogador1 == "X":
                print('\nJogador 1, você será "X"!')
                print('Jogador 2, você será "O"!')
            else:
                print('\nJogador 1, você será "O"!')
                print('Jogador 2, você será "X"!')
            valid = True
        else:
            while valid == False:
                jogador1 = input('Desculpe, não compreendi sua opção, informe novamente(x ou o): ').upper()
                if jogador1 == "X" or jogador1 == "O":
                    if jogador1 == "X":
                        print('\nJogador 1, você será "X"!')
                        print('Jogador 2, você será "O"!')
                    else:
                        print('\nJogador 1, você será "O"!')
                        print('Jogador 2, você será "X"!')
                    valid = True
    return jogador1

#Main
def game(jogador1):
    print("\n\n")
    jogadas1 = []
    jogadas2 = []
    locais1 = ()
    locais2 = ()
    intlocais1 = int()
    intlocais2 = int()
    c = 1
    if jogador1 == "X":
        jogador2 = "O"
    else:
        jogador2 = "X"
    sn = ()
    mapa = ["_","_","_","|","_","_","_","|","_","_","_","\n","_","_","_","|","_","_","_","|","_","_","_","\n"," "," "," ","|"," "," "," ","|"," "," "," "]
    dicmap = {'1':'1','2':'5','3':'9','4':'13','5':'17','6':'21','7':'25','8':'29','9':'33'}
    mapaprint = str()
    input('Vamos começar o jogo! pressione ENTER para continuar ')
    valid = False
    while c <= 9:
        if int(c) % 2 != 0:
            while valid == False:
                locais1 = input("\nJogador 1, escolha onde vai marcar! ")
                try:
                    intlocais1 = int(locais1)
                    if intlocais1<1 and intlocais1>9:
                        print("Favor jogar uma posição válida!(Entre 1 e 9) ")
                    else:
                        if locais1 not in jogadas1 and locais1 not in jogadas2:
                            mapa[int(dicmap[locais1])] = jogador1
                            jogadas1.append(locais1)
                            valid = True
                            c = c+1
                            mapaprint = str()
                            for i in mapa:
                                mapaprint = (mapaprint+str(i))
                            print("\n"+mapaprint)
                            if c >= 6:
                                if mapa[1] == jogador1 and mapa[5] == jogador1 and mapa[9] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[13] == jogador1 and mapa[17] == jogador1 and mapa[21] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[25] == jogador1 and mapa[29] == jogador1 and mapa[33] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[1] == jogador1 and mapa[17] == jogador1 and mapa[33] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[3] == jogador1 and mapa[17] == jogador1 and mapa[25] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[1] == jogador1 and mapa[13] == jogador1 and mapa[25] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[5] == jogador1 and mapa[17] == jogador1 and mapa[29] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                elif mapa[9] == jogador1 and mapa[21] == jogador1 and mapa[33] == jogador1:
                                    print("O jogador 1 ganhou o jogo!")
                                    c = 10
                                else:
                                    if c>9:
                                        print("\nDeu velha!")
                                        c = 10
                                    else:
                                        c = c
                        else:
                            print("Este lugar já foi marcado!")
                except:
                    print("Entrada inválida! Favor inserir apenas números inteiros entre 1 e 9!")
        else:
            while valid == False:
                locais2 = input("\nJogador 2, escolha onde vai marcar! ")
                try:
                    intlocais2 = int(locais2)
                    if intlocais2<1 or intlocais2>9:
                        print("Favor jogar uma posição válida!(Entre 1 e 9) ")
                    else:
                        if locais2 not in jogadas2 and locais2 not in jogadas1:
                            mapa[int(dicmap[locais2])] = jogador2
                            jogadas2.append(locais2)
                            valid = True
                            c = c+1
                            mapaprint = str()
                            for i in mapa:
                                mapaprint = (mapaprint+str(i))
                            print("\n"+mapaprint)
                            if mapa[1] == jogador2 and mapa[5] == jogador2 and mapa[9] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[13] == jogador2 and mapa[17] == jogador2 and mapa[21] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[25] == jogador2 and mapa[29] == jogador2 and mapa[33] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[1] == jogador2 and mapa[17] == jogador2 and mapa[33] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[9] == jogador2 and mapa[17] == jogador2 and mapa[25] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[1] == jogador2 and mapa[13] == jogador2 and mapa[25] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[5] == jogador2 and mapa[17] == jogador2 and mapa[29] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            elif mapa[9] == jogador2 and mapa[21] == jogador2 and mapa[33] == jogador2:
                                print("O jogador 2 ganhou o jogo!")
                                c = 10
                            else:
                                if c>9:
                                    print("\nDeu velha!")
                                    c = 10
                                else:
                                    c = c
                        else:
                            print("Este lugar já foi marcado!")
                except:
                    print("Entrada inválida! Favor inserir apenas números inteiros entre 1 e 9!") 
        valid = False
        
sn = "s"
while sn == "s": 
    valid = False
    begin()
    jogador1 = player(jogador1)
    game(jogador1)
    while valid == False:
        sn = input("\nDeseja jogar novamente?(s/n): ").lower()
        if sn == "s" or sn == "n":
            valid = True
        else:
            print("Erro na entrada de dados, digite apenas 's' ou 'n'! \n")
