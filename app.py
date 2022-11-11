from FONTES.funcoes import *
import os

def main():
    os.system("cls")
    SALDO = init()
    while True:
        #QUAIS DADOS
        DADOS = bd.buscaNaoPago()
        TOTAL_GASTO = float(DADOS['valor'].sum())
        SALDO_FINAL = SALDO - TOTAL_GASTO
        
        menuOpcoes()
        op = input("Digite a opção desejada...: ")
        
        os.system("cls")
        match op:
            case '1':
                pegaDadosGasto(1)
                
            case '2':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)
                pressioneParaContinuar()          
                
            case '3':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)
                excluiGasto(DADOS['rowid'].max())
                
            case '4':
                operacaoArquivo = menuGeraArquivo()
                gera_arquivo(DADOS=DADOS, tipoArquivo=operacaoArquivo, TOTAL_GASTO=TOTAL_GASTO)    
                pressioneParaContinuar()
                
            case '5':
                imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL)
                print()
                id = input('Digite o ID do gasto que deseja atualizar..: ')
                pegaDadosGasto(2, id=id)
                pressioneParaContinuar()
                
            case '6':
                print('SAINDO!')
                pressioneParaContinuar()
                break
            
            case _:
                print('OPÇÃO INVÁLIDA.')
                pressioneParaContinuar()
                    
main()

print()
