import os

def menuCategoria():
    print('DIGITE UMA OPÇÃO PARA CATEGORIA [PADRÃO: OUTROS]')
    print('1 - BANCOS')
    print('2 - DOMÉSTICO')

def menuOpcoes():
        os.system("cls")
        print('*' * 80)
        print('SISTEMA DE CONTROLE DE GASTOS')
        print('*' * 80)
        
        print("[1 - CADASTRAR UM GASTO]")
        print("[2 - EXIBIR MEUS GASTOS]")
        print("[3 - EXCLUIR REGISTRO]")
        print("[4 - SALVAR EM UM ARQUIVO [EXCEL - TXT]]")
        print("[5 - ATUALIZAR UM GASTO]")
        print("[6 - SAIR]")

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
        
        
    