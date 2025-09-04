## API simples em Python (FastAPI) para Render

Esta API expõe dois endpoints GET:

- `GET /health` → retorna `{ "status": "ok" }`.
- `GET /me` → retorna informações do aluno (nome, e-mail, curso, GitHub, cidade e interesses).

Implementada com FastAPI e preparada para rodar localmente e no Render.

### Como rodar localmente

Requisitos: Python 3.11+ (recomendado), Windows PowerShell.

1) Crie e ative o ambiente virtual (VS Code já configurou `.venv` automaticamente). Se precisar criar manualmente:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2) Instale as dependências:

```powershell
pip install -r requirements.txt
```

3) (Opcional) Defina variáveis de ambiente com seus dados para o endpoint `/me`:

```powershell
$env:ME_NAME = "Seu Nome"
$env:ME_EMAIL = "seu.email@example.com"
$env:ME_COURSE = "Seu Curso"
$env:ME_GITHUB = "https://github.com/seuusuario"
$env:ME_CITY = "Sua Cidade"
$env:ME_INTERESTS = "Python,APIs,Cloud"
```

4) Inicie a API:

```powershell
uvicorn app.server:app --reload --port 8000
```

5) Teste no navegador ou via curl:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/me

Documentação interativa: http://127.0.0.1:8000/docs

### Estrutura

- `app/main.py` → definição dos endpoints.
- `app/server.py` → ponto de entrada ASGI (usado por Uvicorn/Render).
- `requirements.txt` → dependências.
- `render.yaml` → configuração para deploy no Render.
- `tests/test_app.py` → testes simples dos endpoints.

### Deploy no Render

Opção A: Usar o arquivo `render.yaml` (Infra as Code)

1) Faça push deste repositório público no GitHub.
2) No Render, escolha New → Blueprint → conecte seu repositório.
3) Confirme o serviço web sugerido. O Render usará:
	- Build Command: `pip install -r requirements.txt`
	- Start Command: `uvicorn app.server:app --host 0.0.0.0 --port $PORT`
4) Ajuste as variáveis de ambiente (ME_NAME, etc.) no painel do Render, se desejar.
5) Crie o serviço e aguarde o deploy.

Opção B: Deploy manual (Web Service)

1) New → Web Service → conecte o repositório.
2) Runtime: Python. Build: `pip install -r requirements.txt`.
3) Start: `uvicorn app.server:app --host 0.0.0.0 --port $PORT`.
4) Adicione as env vars conforme necessário.

### URL pública no Render

Após o deploy, atualize aqui com a URL pública do serviço:

API pública: https://api-deploy-no-render.onrender.com/docs

Endpoints:

- https://api-deploy-no-render.onrender.com/health
- https://api-deploy-no-render.onrender.com/me

### Testes

Execute os testes localmente:

```powershell
pytest -q
```

### Licença

Veja o arquivo `LICENSE`.

# API-Deploy-no-Render
API simples em Python com dois endpoints do tipo GET
