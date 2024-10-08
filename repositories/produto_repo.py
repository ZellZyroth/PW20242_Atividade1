from typing import Optional
from models.produto_model import Produto
from sql import produto_sql
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR, SQL_OBTER_TODOS
from util import obter_conexao


def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)


def inserir(produto: Produto) -> Optional[Produto]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(
            SQL_INSERIR,
            (
                produto.nome,
                produto.descricao,
                produto.estoque,
                produto.preço,
                produto.categoria,
            ),
        )
    if db.rowcount > 0:
        produto.id = db.lastrowid
        return produto
    else:
        return None


def obter_todos():
    bd = obter_conexao.cursor()
    bd.execute(produto_sql.SQL_OBTER_TODOS)