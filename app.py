from FONTES.funcoes import *
from FONTES.menus import *
from FONTES.menuPrincipal import menuPrincipal

import os

def main():
    os.system("cls")
    SALDO = init()
    opcaoDado = menuTipoDado()
    opcao, descricao = opcaoDado 
    
    while True:   
        DADOS = tipoDataFrame(opcao)
        TOTAL_GASTO = float(DADOS['valor'].sum())
        SALDO_FINAL = SALDO - TOTAL_GASTO     
        menuPrincipal(descricao)
        print(cores.reset_color)
        op = input("..: ")

        os.system("cls")
        match op:
            case '1':
                pegaDadosGasto(1)
                
            case '2':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)       
                
            case '3':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)
                id = validaID()
                excluiGasto()
                
            case '4':
                operacaoArquivo = menuGeraArquivo()
                gera_arquivo(DADOS=DADOS, tipoArquivo=operacaoArquivo, TOTAL_GASTO=TOTAL_GASTO, descricao=descricao)    
                
            case '5':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)
                print()
                id = validaID(1)
                pegaDadosGasto(2, id=id)
            
            case '6':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)
                print()
                id = validaID(1)
                atualizaRegistroPago(id)
                pressioneParaContinuar()
                
            case '7':
                menuTipoDado()
                break
            
            case '8':
                print('SAINDO!')
                pressioneParaContinuar()
                break
            
            case _:
                print('OPÇÃO INVÁLIDA.')
                pressioneParaContinuar()
                    
main()