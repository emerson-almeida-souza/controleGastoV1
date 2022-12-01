import BANCO.banco as bd
from FONTES.menus import *
from FONTES.menuCategoriaGasto import menuCategoriaGasto
import pandas as pd

def atualizaRegistroPago(id):
    try: 
        bd.excluiRegistroBd(id)
        print('REGISTRO ATUALIZADO COM SUCESSO!')
    except:
        print('FALHA AO ATUALIZAR. O ID FORNECIDO É INVÁLIDO. FORNCEÇA UM ID VÁLIDO.')

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
        
        valor = validaValorDivida()
        print('-' * 80)
        
        menuCategoriaGasto()
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
            try:
                bd.atualizaRegistro(id, nomeGasto=nomeGasto, valor=valor, categoria = categoria ,limiteGasto=limiteGasto, vencimentoDia=vencimentoDia, pago=pago)
                print("GASTO ATUALIZADO COM SUCESSO!")
                pressioneParaContinuar()
            except:
                print('ID do registro não encontrado, por favor forneceça um ID válido.')
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

def gerarTxt(DADOS, TOTAL_GASTO, descricao):
    try:
        nomeArquivo = f'ARQUIVOS\{descricao}.txt'
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.write(f"{DADOS[['nome', 'valor', 'categoria', 'limiteGasto', 'vencimentoDia', 'pago']].to_markdown(index=False).upper()} \n\n TOTAL DIVIDAS: R$ {TOTAL_GASTO}")
                        
            print(f"Arquivo salvo com sucesso em: {os.getcwd()}\\{nomeArquivo}")
            pressioneParaContinuar()
    except:
        print("ERRO AO SALVAR O ARQUIVO, CONTATE O ADMINISTRADOR")
        pressioneParaContinuar()

def excluiGasto(id):
    try: 
        bd.excluiRegistroBd(id)
        print('REGISTRO EXCLUIDO COM SUCESSO!')
        pressioneParaContinuar()
    except:
        print('FALHA AO EXCLUIR. O ID FORNECIDO É INVÁLIDO. FORNCEÇA UM ID VÁLIDO.')
        pressioneParaContinuar()

def imprimirDados(DADOS, TOTAL_GASTO, SALDO, SALDO_FINAL):
    print(DADOS.to_markdown(index=False).upper())
    print(f'\nTOTAL DIVIDAS: R$ {round(TOTAL_GASTO, 2)}')
    print(f'Meu saldo atual é de: R$ {SALDO}')
    print(f'Saldo pós pagamento: R$ {round(SALDO_FINAL, 2)}')
    pressioneParaContinuar()

def gerar_excel(DADOS, descricao):
    # df2 = DADOS.copy()
    with pd.ExcelWriter(f'ARQUIVOS\{descricao}.xls') as writer:  
        DADOS.to_excel(writer, sheet_name=F"TOTAL GASTO R${round(DADOS['valor'].sum(), 2)}", index=False)
        # df2.to_excel(writer, sheet_name='Sheet_name_2')

def gera_arquivo(tipoArquivo, DADOS, TOTAL_GASTO, descricao):
    if tipoArquivo == 1:
        gerarTxt(DADOS, TOTAL_GASTO, descricao)
        pressioneParaContinuar()
    elif tipoArquivo == 2:
        gerar_excel(DADOS, descricao)
        pressioneParaContinuar()

def validaValorDivida():
    while True:
        v = input("DIGITE O VALOR[EX: 50.0]..: ")
        if type(v) == str:
            try:
                valor = float(v)
                break
            except:
                print(f'Erro ao converter o {v} para moeda, tente novamente seguindo o padrão[EX: 50.0]')
                pressioneParaContinuar()
                
    return valor