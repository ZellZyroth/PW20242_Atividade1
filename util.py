import sqlite3

def Obter_Conexao():
    return sqlite3.connect("dados.db")
