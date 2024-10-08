from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

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
    return RedirectResponse("/", 303)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)