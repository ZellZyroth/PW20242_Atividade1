from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from models.produto_model import Produto
from repositories.produto_repo import Criar_Tabela, Inserir

Criar_Tabela()
print("Criou Tabela")

NOME_PASTA_STATIC="static/"

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})


@app.post("/post_cadastro")
def post_cadastro(
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...),
    categoria: str = Form(...)):
    
    produto = Produto (
        nome=nome,
        descricao=descricao,
        estoque=estoque,
        preco=preco,
        categoria=categoria
)
    produto_inserido = Inserir(produto)

    if produto_inserido:
        return RedirectResponse("/cadastro_recebido", status_code=303)
    else:
        return RedirectResponse("/cadastro", status_code=303)


@app.get("/cadastro_recebido")
def get_cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)