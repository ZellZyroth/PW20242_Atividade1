from typing import Optional
from models.produto_model import Produto
from sql import produto_sql
from sql.produto_sql import *
from util import Obter_Conexao


def Criar_Tabela():
    with Obter_Conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)


def Inserir(produto: Produto) -> Optional[Produto]:
    with Obter_Conexao() as conexao:
        db = conexao.cursor()
        db.execute(
            SQL_INSERIR,
            (
                produto.nome,
                produto.descricao,
                produto.estoque,
                produto.preco,
                produto.categoria,
            ),
)
    if db.rowcount > 0:
        produto.id = db.lastrowid
        return produto
    else:
        return None


def Obter_Todos():
    bd = Obter_Conexao.cursor()
    bd.execute(produto_sql.SQL_OBTER_TODOS)
