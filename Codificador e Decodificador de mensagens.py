##importação de módulos
import random
import math

##Definição de variáveis e funções
input('\nEste programa irá codificar uma mensagem curta e poderá ser usado para decofica-la mediante inserção de uma chave de acesso.\nPara começar, pressione Enter.')
var = float()
chave = float()
encrypt = []
senha = int()
chave = []
literal = []
dic_literal = {}
dic_decrypt = {}

def cript_texto (chave,literal,encrypt):
    valid_texto = False
    while valid_texto == False:
        texto = input('\n\nDigite uma mensagem de até 10 caracteres a ser codificada: ')
        if len(texto)>10:
            print('Mensagem superior a 10 caracteres ou com caracteres especiais. Favor inserir novamente.')
        else:
            valid_texto = True
    carac = len(texto)
    chave = []
    cont = 0
    while cont < carac:
        literal.append(texto[cont])
        chave.append(cont)
        cont = cont+1
    cont = 0
    random.shuffle(chave)
    input('\n\nPressione Enter para receber sua chave de acesso. Com ela, poderá decodificar sua mensagem.\n\n')
    str_chave = [str(i) for i in chave]
    print('>>>>>>'+''.join(str_chave)+'<<<<<<\n\n')
    while cont < len(chave):
        encrypt.append(literal[chave[cont]])
        cont = cont + 1
    input('\n\nPressione Enter para visualizar sua mensagem codificada. ')
    input('\nEsta é sua mensagem codificada >>>>>>'+(''.join(encrypt))+'<<<<<< (Os espaços também fazem parte da mensagem) Pressione Enter novamente.')
    return encrypt

def decript_texto (literal,encrypt,dic_literal,dic_decrypt):
    encrypt = input('\n\nFavor inserir a mensagem codificada: ')
    chave_str = input('\nInsira a chave de acesso: ')
    cont = 0
    chave = []
    chaves = []
    valores = []
    for i in range(len(chave_str)):
        chave.append(int(chave_str[cont]))
        cont = cont+1
    cont = 0
    for i in chave:
        dic_literal[chave[cont]] = encrypt[cont]
        cont = cont+1
    for i in dic_literal:
        chaves.append(i)
    chaves = sorted(chaves)
    for i in chaves:
        dic_decrypt[chaves[i]] = dic_literal[chaves[i]]
    for i in dic_decrypt:
        valores.append(dic_decrypt[i])
    input('\nPressione enter para visualizar a mensagem decodificada.\n\n')
    print('>>>>>>'+''.join(valores)+'<<<<<<')
    
##Início do Programa.
valid_answer = False
while valid_answer == False:
    r = input('\n\nDigite "C" para codificar um programa ou "D" para decodificar: ').lower()
    if r == 'c':
        chave = cript_texto(chave,literal,encrypt)
        valid_repetir = False
        while valid_repetir == False:
            repetir = input('\n\nDeseja usar o programa novamente?(s/n): ').lower()
            if repetir == 's':
                valid_repetir = True
            elif repetir == 'n':
                valid_repetir = True
                valid_answer = True
            else:
                print('\nDesculpe, não entendi a informação. Poderia digitar novamente?\n')
    elif r == 'd':
        decript_texto (literal,encrypt,dic_literal,dic_decrypt)
        valid_repetir = False
        while valid_repetir == False:
            repetir = input('\n\nDeseja usar o programa novamente?(s/n): ').lower()
            if repetir == 's':
                valid_repetir = True
            elif repetir == 'n':
                valid_repetir = True
                valid_answer = True
            else:
                print('\nDesculpe, não entendi a informação. Poderia digitar novamente?\n')
    else:
        print('\nDesculpe, não entendi a informação. Poderia digitar novamente?\n')
            
input('\n\n\nPressione Enter para sair.')
