# devops-api

Projeto de portfólio DevOps: uma API REST pequena em Python que serve de base para praticar todo o caminho **do commit ao deploy** — testes automatizados, containers, pipeline de CI/CD, infraestrutura como código e monitoramento.

> 🚧 Projeto em construção. O roadmap abaixo mostra o que já está pronto e o que vem a seguir.

## Stack

| Camada | Ferramenta |
|---|---|
| Aplicação | Python 3.12, FastAPI, Uvicorn |
| Banco de dados | PostgreSQL (psycopg) |
| Qualidade | pytest, httpx, ruff |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Infraestrutura | Terraform, cloud-init |
| Observabilidade | Prometheus, Grafana |

## Roadmap

- [x] API com endpoint de health check (`GET /health`)
- [x] Teste automatizado do health check com pytest
- [ ] Dockerfile e `.dockerignore`
- [ ] Docker Compose com API + PostgreSQL
- [ ] Pipeline de CI no GitHub Actions (lint + testes a cada push)
- [ ] Publicação da imagem em registry (CD)
- [ ] Provisionamento de servidor com Terraform + cloud-init
- [ ] Métricas com Prometheus e dashboard no Grafana

## Estrutura

```
app/            código da API (FastAPI)
tests/          testes automatizados (pytest)
infra/          infraestrutura como código (Terraform, cloud-init)
monitoring/     configuração do Prometheus e do Grafana
.github/        workflows do GitHub Actions
```

## Como rodar localmente

Pré-requisito: Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt

uvicorn app.main:app --reload    # API em http://localhost:8000
```

Teste rápido:

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

A documentação interativa da API fica em http://localhost:8000/docs.

## Testes e lint

```bash
pytest
ruff check .
```

## Autor

**Rafael Siqueira de Oliveira** — graduando em Engenharia Eletrônica (CEFET/RJ) em transição para DevOps.
[LinkedIn](https://linkedin.com/in/rafael-oliveira-74666072) · [GitHub](https://github.com/HieiMaster23)
