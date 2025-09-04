from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Aluno API", version="1.0.0")


@app.get("/", include_in_schema=False)
def root():
    """Página inicial simples para evitar 404 na raiz."""
    return {
        "message": "Aluno API em execução",
        "try": ["/health", "/me", "/docs"],
    }


@app.get("/health", summary="Healthcheck")
def health():
    """Retorna o status da aplicação."""
    return {"status": "ok"}


def _get_env(key: str, default: str = "") -> str:
    value = os.getenv(key)
    return value if value is not None and value != "" else default


@app.get("/me", summary="Informações do aluno")
def me():
    """
    Retorna informações do aluno. Pode ser configurado via variáveis de ambiente:
    ME_NAME, ME_EMAIL, ME_COURSE, ME_GITHUB, ME_CITY, ME_INTERESTS (separados por vírgula)
    """
    interests_raw = _get_env("ME_INTERESTS", "Python,APIs,Cloud")
    interests = [i.strip() for i in interests_raw.split(",") if i.strip()]
    data = {
        "name": _get_env("ME_NAME", "Seu Nome"),
        "email": _get_env("ME_EMAIL", "seu.email@example.com"),
        "course": _get_env("ME_COURSE", "Seu Curso"),
        "github": _get_env("ME_GITHUB", "https://github.com/seuusuario"),
        "city": _get_env("ME_CITY", "Sua Cidade"),
        "interests": interests,
    }
    return JSONResponse(content=data)


if __name__ == "__main__":
    # Execução direta: uvicorn integrado (útil para debug local rápido)
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
