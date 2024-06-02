# Mock API Brasilprev


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- [x] Acesso a um computador com Python
- [x] Terminal Linux/Mac (ou WSL)
- [x] Docker e docker compose
- [x] Editor de código de sua preferência (VSCode, vim, micro, emacs)


## 🚀 Instalando API Brasilprev

```
$ cd pasta/onde/vc/guarda/seus/projetos
$ git git@github.com:evaristofm/api-brasilprev.git

```

próximo passo: no diretorio raiz do repositório executar:


```
docker compose up -d --build

```

próximo passo: execute as migraões do projeto usando docker compose + alembic


```
docker compose exec api prev alembic upgrade head

```

Acessando a documentação SWAGGER da API

```
http://localhost:8000/docs

```
