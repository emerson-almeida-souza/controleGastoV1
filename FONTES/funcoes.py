import BANCO.banco as bd
from FONTES.menus import *
import pandas as pd

def vencimentoGasto(vencimento):
    if vencimento != 5 and vencimento != 15:
        vencimento = 5
    return vencimento

def pagoGasto(pago):
    if pago != 0 or pago != 1:
        pago = 0
    return pago

def categoriasGasto(opCategoriaGasto):
    if opCategoriaGasto == 1:
        nomeCategoria = 'BANCOS'
    elif opCategoriaGasto == 2:
        nomeCategoria = 'DOMESTICO'
    else:
        nomeCategoria = 'OUTROS'
        
    return nomeCategoria

def pegaDadosGasto(operacao, id=None):
    try:
        print('-' * 80)
        nomeGasto = str(input("NOME DO GASTO [EX: CONTA DE LUZ]..: ")).upper()
        print('-' * 80)
        
        valor = float(input("VALOR [EX: 50.0]..: "))
        print('-' * 80)
        
        menuCategoria()
        opCategoria = int(input('..: ')) 
        categoria = categoriasGasto(opCategoria)
        print('-' * 80)
        
        limiteGasto = float(input("LIMITE DE GASTO MENSAL [EX: 50]..: "))
        print('-' * 80)
        
        menuVencimento()
        opVencimentoDia = int(input("..: "))
        vencimentoDia = vencimentoGasto(opVencimentoDia)
        print('-' * 80)
        
        menuPago()
        opPago = int(input("..: "))
        pago = pagoGasto(opPago)
        print('-' * 80)
        
        if operacao == 1:
            cadastraGasto(nomeGasto=nomeGasto, valor=valor, categoria = categoria ,limiteGasto=limiteGasto, vencimentoDia=vencimentoDia, pago=pago)
            print("GASTO INSERIDO COM SUCESSO!")
            pressioneParaContinuar()
        elif operacao == 2:
            bd.atualizaRegistro(id, nomeGasto=nomeGasto, valor=valor, categoria = categoria ,limiteGasto=limiteGasto, vencimentoDia=vencimentoDia, pago=pago)
            print("GASTO ATUALIZADO COM SUCESSO!")
            pressioneParaContinuar()

    except ValueError as erro:
        print(f"Valor inválido: {erro}")
        pressioneParaContinuar()
                    
    except TypeError as erro:
        print(erro)
        pressioneParaContinuar()
        
    except:
        print('ERRO DESCONHECIDO, CONTATE O ADMINISTRADOR.')
        pressioneParaContinuar()

def cadastraGasto(nomeGasto, valor, categoria, limiteGasto, vencimentoDia, pago):
    if nomeGasto == '':
        raise ValueError('Não foi possivel cadastrar o gasto [O campo [NOME DO GASTO] está vazio].')  
    if categoria == '':
        raise ValueError('Não foi possivel cadastrar o gasto [O campo [CATEGORIA] está vazio].')  

    if vencimentoDia != 5 and vencimentoDia != 15:
        raise ValueError('Não foi possivel cadastrar o gasto [O dia do vencimento deve ser: [5 ou 15]].')
    
    if pago != 0 and pago != 1:
        raise ValueError('Não foi possivel cadastrar o gasto [O campo PAGO ? deve ser: [[0]->Não Pago ou [1]->Pago]].')
    else:
        bd.inserirTabela(nome=nomeGasto, valor=valor, limiteGasto=limiteGasto, categoria=categoria, pago=pago, vencimentoDia=vencimentoDia)

def gerarTxt(DADOS, TOTAL_GASTO):
    try:
        nomeArquivo = r'ARQUIVOS\balanco.txt'
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.write(f"{DADOS[['nome', 'valor', 'categoria', 'limiteGasto', 'vencimentoDia', 'pago']].to_markdown(index=False).upper()} \n\n TOTAL DIVIDAS: R$ {TOTAL_GASTO}")
                        
            print(f"Arquivo salvo com sucesso em: {os.getcwd()}\\{nomeArquivo}")
            pressioneParaContinuar()
    except:
        print("ERRO AO SALVAR O ARQUIVO, CONTATE O ADMINISTRADOR")
        pressioneParaContinuar()

def excluiGasto(ultimoId):
    try:
        print('DIGITE O ID DO REGISTRO PARA EXCLUIR')
        id = int(input('..: '))
        excluiRegistro(id, ultimoId)
        
        print('REGISTRO EXCLUIDO COM SUCESSO')
        pressioneParaContinuar()
        
    except ValueError as erro:
        print(erro) 
        pressioneParaContinuar()
    except:
        print('ERRO DESCONHECIDO, CONTATE O ADMINISTRADOR.')
        pressioneParaContinuar()

def excluiRegistro(id, ultimoId):
    if id > ultimoId or id < 0:
        raise ValueError('ID de gasto inválido, por favor digite o ID correto do gasto')
    else:
        bd.excluiRegistroBd(id)

def imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL):
    print(DADOS.to_markdown(index=False).upper())
    print(f'\nTOTAL DIVIDAS: R$ {round(TOTAL_GASTO, 2)}')
    print(f'Meu saldo atual é de: R$ {SALDO}')
    print(f'Saldo pós pagamento: R$ {round(SALDO_FINAL, 2)}')
    print()

def gerar_excel(DADOS):
    # df2 = DADOS.copy()
    with pd.ExcelWriter('ARQUIVOS\GASTOS.xls') as writer:  
        DADOS.to_excel(writer, sheet_name=F"TOTAL GASTO R${round(DADOS['valor'].sum(), 2)}", index=False)
        # df2.to_excel(writer, sheet_name='Sheet_name_2')

def gera_arquivo(tipoArquivo, DADOS, TOTAL_GASTO):
    if tipoArquivo == 1:
        gerarTxt(DADOS, TOTAL_GASTO)
    elif tipoArquivo == 2:
        gerar_excel(DADOS)