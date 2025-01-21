from fastapi import FastAPI, HTTPException, Query
import requests
from urllib.parse import urlparse, urlunparse

app = FastAPI()

def adicionar_protocolo(url: str) -> str:
    """
    Valida e ajusta a URL, adicionando o protocolo (http:// ou https://) caso necessário.
    """
    parsed = urlparse(url)

    if not parsed.netloc:
        if parsed.path:
            parsed = urlparse(f"http://{url}")
        else:
            raise HTTPException(status_code=400, detail=f"URL inválida: {url}")

    if not parsed.scheme:
        parsed = parsed._replace(scheme="http")

    return urlunparse(parsed)

@app.get("/check-site")
async def check_site(url: str = Query(..., description="URL do site a ser verificado")):
    """
    Verifica se um site está funcionando.

    Parâmetros:
        - url: URL do site a ser verificado (ex: https://example.com).
    Retorna:
        - status: Mensagem indicando se o site está acessível ou não.
    """
    try:
        url = adicionar_protocolo(url)  # Adiciona e valida o protocolo
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return {"status": "Site está funcionando!", "url": url}
        else:
            return {"status": f"Site respondeu com status {response.status_code}", "url": url}
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Erro ao acessar o site: {e}")