from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Půjčovna Motovozíků Řepiště")

# Připojení statických souborů (CSS, obrázky)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Nastavení složky s HTML šablonami
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Přepsali jsme způsob, jakým voláme TemplateResponse
    return templates.TemplateResponse(request=request, name="index.html")