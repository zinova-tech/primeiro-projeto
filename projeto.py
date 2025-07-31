from modulo_1 import *
import json
from time import sleep
from os import system

dados = list()
futebol  = dict()
bascket = dict()
voleibol = dict()
tenis = dict()
try:
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
except FileNotFoundError:
    dados = []

while True:
    despor = {1:'Futebol',2:'Bascketbol',3:'Voleibol',4:'Tênis'}
    intro = {1:'CADASTRAR NOVA PESSOA', 2:'VER PESSOAS CADASTRADAS', 3:'Eliminar Dados', 4:'SAIR DO PROGRAMA'}
    cabeçalho('BEM VINDO AO FZSPORTS')
    varrerdic(intro)
    lin()
    opc1 = intperson('Sua opção: ')
    while opc1 <= 0 or opc1 > len(intro):
        print(f'{opc1} Está fora da lista, por favor digite uma opção válida!')
        opc1 = intperson('Sua opção: ')

    if opc1 == 1:
        system('clear')
        cabeçalho('NOVO CADASTRO')
        varrerdic(despor)
        lin()
        opc2 = intperson('Sua opção: ')
        while opc2 <= 0 or opc2 > len(despor):
            print(f'{opc2} Está fora da lista, por favor digite uma opção válida!')
            opc2 = intperson('Sua opção: ')

        if opc2 in despor:
            cabeçalho(despor[opc2])   
            if opc2 == 1:
                futebol['Nome'] = str(input('Nome: ')).title()
                for a,b in enumerate(dados): 
                    while futebol['Nome'].title() in dados[a]['Nome']:
                        print('Nome existente!')
                        futebol['Nome'] = str(input('Nome: '))
                futebol['Idade'] = intperson('Idade: ')
                futebol['Desporto'] = despor[opc2]
                cabeçalho('CADASTRADO COM ÊXITO!')
                dados.append(futebol.copy())
            elif opc2 == 2:
                bascket['Nome'] = str(input('Nome: '))
                bascket['Idade'] = intperson('Idade: ')
                bascket['Desporto'] = despor[opc2]
                dados.append(bascket.copy())
            elif opc2 == 3:
                voleibol['Nome'] = str(input('Nome: '))
                voleibol['Idade'] = intperson('Idade: ')
                voleibol['Desporto'] = despor[opc2]
                dados.append(voleibol.copy())
            elif opc2 == 4:
                tenis['Nome'] = str(input('Nome: '))
                tenis['Idade'] = intperson('Idade: ')
                tenis['Desporto'] = despor[opc2]
                dados.append(tenis.copy())
    if opc1 == 2:
        system('clear')
        cabeçalho('PESSOAS CADASTRADAS')
        varrerdic(despor)
        lin()
        opc3 = intperson('Seleione um desporto para ver as pessoas cadastradas: ')
        while opc3 <= 0 or opc3 > len(despor):
            print('Opção fora da lista!')
            opc3 = intperson('Seleione um desporto para ver as pessoas cadastradas: ')
        cabeçalho(despor[opc3])
        a = False
        for b in dados:
            if b['Desporto'] == despor[opc3]:
                print(f'{b["Nome"]} ______________ {b["Idade"]} anos')
                a = True
        if not a:
            print('Nenhuma pessoas cadastrada.')
        sleep(2)
    if opc1 == 3:
        cabeçalho(intro[opc1])
        varrerdic(despor)
        opc3 = intperson('Seleione um desporto para ver as pessoas cadastradas: ')
        while opc3 <= 0 or opc3 > len(despor):
            print('Opção fora da lista!')
            opc3 = intperson('Seleione um desporto para ver as pessoas cadastradas: ')
        lin()
        opc2 = str(input('Nome Do Candidato: ')).title()
        for a,b in enumerate(dados):
            if opc2 in dados[a]['Nome']:
                pos = a
                cabeçalho('Êxito')
                del dados[pos]
            else:
                cabeçalho(f'Não há registro de "{opc2}".')
            
    if opc1 == 4:
        with open("dados.json", "w", encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            cabeçalho('SAÍNDO DO PROGRAMA')
            sleep(2)
        break


