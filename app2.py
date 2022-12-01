import BANCO.banco as bd
from FONTES.menus import *
from FONTES.menuCategoriaGasto import menuCategoriaGasto
import pandas as pd
from PySimpleGUI import Window, Button, Text, Table


DADOS = bd.buscaTudo()
headers = list(DADOS)
dadosGasto = [] #ARMAZENA TODOS OS DADOS
Nlinha = len(headers[0]) + 1
Ncoluna = len(headers)
#print(f'O arquivo tem {Nlinha} Linhas e {Ncoluna} colunas')

for linha in range(Nlinha):  #NAVEGA LINHA POR LINHA
    data = [] #CRIA A LISTA DA LINHA
    for coluna in range(Ncoluna):
        data.append(DADOS[headers[coluna]][linha]) #ADICIONA CADA DADO DA LINHA NA LISTA
        
    dadosGasto.append(data) #ADICIONA VÁRIAS LINHAS NA LIST

print(dadosGasto) 


def telaInicial():
    layout = [
    [Text('SELECIONE O GASTO A SER ANALISADO')],
    [Button('TODOS OS GASTOS', key='-TG-')]
    
]
    return Window('CONTROLE DE GASTOS', layout=layout, element_justification='c')

def menuOpcoes():
    layout = [
    [Text('SELECIONE A OPÇÃO')],
    [Button('VISUALIZAR TODOS OS GASTOS', key='-VTG-')]
    
]
    return Window('CONTROLE DE GASTOS', layout=layout, element_justification='c')

def exibirDados(DADOS):
    layout = [
    [Text('TODOS OS GASTOS')],
    [Table(values=DADOS, headings=headers)]
]
    return Window('CONTROLE DE GASTOS', layout=layout, element_justification='c')

window = telaInicial()

while True:
    event, values = window.read()
    print(event, values)

    match(event):
        case '-TG-' | '-VTG-':
            window.close()
            match(event):
                case '-TG-':
                   window = menuOpcoes()
                   
                case '-VTG-':
                    print('cai no vtg')
                    window = exibirDados(dadosGasto)
                   
        case None:
            print('Fechei, recebi None')
            break
        case _:
            print(event, values)

window.close()