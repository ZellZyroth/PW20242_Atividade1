from dataclasses import dataclass
from typing import Optional

@dataclass
class Produto:
    id: Optional[str] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    estoque: Optional[str] = None
    preco: Optional[str] = None
    categoria: Optional[str] = None
