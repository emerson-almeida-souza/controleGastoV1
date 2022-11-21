import sqlite3
import pandas as pd 
import datetime as dt

DATA_ATUAL = dt.date.today()


con = sqlite3.connect('BANCO/Gastos.db')

cur = con.cursor()

def criarTabela():
    cur.execute(f"""
        CREATE TABLE Gasto(
        nome VARCHAR NOT NULL DEFAULT 'NOME_GASTO', 
        valor DOUBLE NOT NULL,
        categoria VARCHAR NOT NULL DEFAULT 'NOME_CATEGORIA',
        limiteGasto DOUBLE NOT NULL DEFAULT 0,
        mes INT NOT NULL DEFAULT {DATA_ATUAL.month},
        ano INT NOT NULL DEFAULT {DATA_ATUAL.year},
        vencimentoDia INT NOT NULL DEFAULT 5,
        pago INT NOT NULL DEFAULT 0
        )
        """)

def inserirTabela(nome, valor, categoria, limiteGasto, vencimentoDia, pago):
    cur.execute(f"INSERT INTO Gasto (nome, valor, categoria, limiteGasto, vencimentoDia, pago) VALUES (?, ?, ?, ?, ?, ?)", (nome, valor, categoria, limiteGasto, vencimentoDia, pago))
    con.commit() 

def buscaTudo():
    sql = 'SELECT ROWID, * FROM Gasto'
    data_SQL = pd.read_sql(sql, con)
    data = pd.DataFrame(data_SQL)
    return data

def buscaDia15():
    sql = 'SELECT ROWID, * FROM Gasto WHERE vencimentoDia = 15'
    data_SQL = pd.read_sql(sql, con)
    data = pd.DataFrame(data_SQL)
    return data

def buscaDia5():
    sql = 'SELECT ROWID, * FROM Gasto WHERE vencimentoDia = 5'
    data_SQL = pd.read_sql(sql, con)
    data = pd.DataFrame(data_SQL)
    return data

def buscaPago():
    sql = 'SELECT ROWID, * FROM Gasto WHERE pago = 1'
    data_SQL = pd.read_sql(sql, con)
    data = pd.DataFrame(data_SQL)
    return data

def buscaNaoPago():
    sql = 'SELECT ROWID, * FROM Gasto WHERE pago = 0'
    data_SQL = pd.read_sql(sql, con)
    data = pd.DataFrame(data_SQL)
    return data

def atualizaRegistro(id, nomeGasto, valor, categoria, limiteGasto, vencimentoDia, pago):    
    cur.execute(f"UPDATE Gasto set nome = ?, valor = ?, categoria = ?, limiteGasto = ?, vencimentoDia = ?, pago = ? WHERE rowid = ?", (nomeGasto, valor, categoria, limiteGasto, vencimentoDia, pago, id))
    con.commit() 

def atualizaPago(id):    
    cur.execute(f"UPDATE Gasto set pago = 1 WHERE rowid = ?", (id))
    con.commit() 

def buscaUm(id):
    res = cur.execute('select nome, valor, categoria, limiteGasto, vencimentoDia, pago from Gasto where rowid = ?', (id, )).fetchone()
    return res
    
def excluiRegistroBd(id):
    cur.execute(f"delete from Gasto where ROWID = ?", (id, ))
    con.commit() #Confirmar alterações 

dados = buscaTudo()



#inserir colunas pandas
# dados.insert(loc=8, column='teste', value='teste')
# print(dados)
# #UNPACK PYTHON
# nome, valor, categoria, limiteGasto, vencimentoDia, pago = res

# #PACK
# pack = nome, valor, categoria, limiteGasto, vencimentoDia, pago
# print(pack)


    
# def varias_abas_excel():
#     df2 = DADOS.copy()
#     with pd.ExcelWriter('GASTOS.xls') as writer:  
#         dados.to_excel(writer, sheet_name='Sheet_name_1')
#         df2.to_excel(writer, sheet_name='Sheet_name_2')



    




