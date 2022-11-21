import os
from FONTES.funcoes import *
import BANCO.banco as bd

def menuCategoria():
    print('DIGITE UMA OPÇÃO PARA CATEGORIA [PADRÃO: OUTROS]')
    print('1 - BANCOS')
    print('2 - DOMÉSTICO')

def menuOpcoes(descricao):
        os.system("cls")
        print('*' * 80)
        print('SISTEMA DE CONTROLE DE GASTOS')
        print(f'GASTO ANALISADO: {descricao}')
        print('*' * 80)
        
        print("[1 - CADASTRAR UM GASTO]")
        print("[2 - EXIBIR MEUS GASTOS]")
        print("[3 - EXCLUIR REGISTRO]")
        print("[4 - SALVAR EM UM ARQUIVO [EXCEL - TXT]]")
        print("[5 - ATUALIZAR UM GASTO]")
        print("[6 - MARCAR GASTO COMO PAGO]")
        print("[7 - SAIR]")

def pressioneParaContinuar():
    input("Pressione qualquer tecla para continuar... ")
    os.system("cls")

def menuVencimento():
    print('DIGITE O DIA DE VENCIMENTO [PADRÃO: DIA 5]')
    print('5 - DIA 5')
    print('15 - DIA 15')

def menuPago():
    print('O GASTO FOI PAGO ? [PADRÃO: NÃO]')
    print('1 - SIM')
    print('2 - NÃO')

def init():
    saldo = float(input("Digite seu saldo atual...: "))
    pressioneParaContinuar()
    return saldo

def menuGeraArquivo():
    while True:
        try:
            os.system('cls')
            print('1 - TXT')
            print('2 - EXCEL')
            op = int(input('Digite uma opcão..: '))

            if op != 1 and op != 2:
                os.system('cls')
                print('ERRO: DIGITE UMA OPÇÃO VÁLIDA.')
                pressioneParaContinuar()
            else:
                break
        except:
            os.system('cls')
            print('ERRO: DIGITE UMA OPÇÃO VÁLIDA.')
            pressioneParaContinuar()  
    return op

def validaID(operacao):
    if operacao == 1:
        try:
            id = int(input('Digite o ID do gasto que deseja ATUALIZAR..: '))
        except:
            print("ERRO, O ID DIGITADO É INVÁLIDO, TENTE NOVAMENTE COM UM ID VÁLIDO.")
            pressioneParaContinuar()
    if operacao == 2:
        try:
            id = int(input('Digite o ID do gasto que deseja marcar como pago..: '))
        except:
            print("ERRO, O ID DIGITADO É INVÁLIDO, TENTE NOVAMENTE COM UM ID VÁLIDO.")
            pressioneParaContinuar()
            
    return id

def menuTipoDado():
    print('ESCOLHA OS GASTOS PARA AS OPERAÇÕES')
    print('1 - TODOS OS GASTOS')
    print('2 - GASTOS PAGOS')
    print('3 - GASTOS NÃO PAGOS')
    print('4 - GASTOS DIA 5')
    print('5 - GASTOS DIA 15')
    
    print('DIGITE A OPÇÃO')
    op = input('..: ')
    
    nomeOpcao = [None] * 2
    nomeOpcao[0] = op
    while True:
        match op:
            case '1':
                nomeOpcao[1] = 'TODOS OS GASTOS'
                break
            case '2':
                nomeOpcao[1] = 'GASTOS PAGOS'
                break
            case '3':
                nomeOpcao[1] = 'GASTOS NÃO PAGOS'
                break
            case '4':
                nomeOpcao[1] = ' GASTOS DIA 5'
                break
            case '5':
                nomeOpcao[1] = 'GASTOS DIA 15'
                break
            case _:
                print('OPÇÃO INVÁLIDA')
    return nomeOpcao
    
def tipoDataFrame(op):
    while True:
        match op:
            case '1':
                DADOS = bd.buscaTudo()
                break
            case '2':
                DADOS = bd.buscaPago()
                break
            case '3':
                DADOS = bd.buscaNaoPago()
                break
            case '4':
                DADOS = bd.buscaDia5()
                break
            case '5':
                DADOS = bd.buscaDia15()
                break
            case _:
                print('OPÇÃO INVÁLIDA')
                
    pressioneParaContinuar()
    return DADOS
