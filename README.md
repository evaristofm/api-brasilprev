# Mock API Brasilprev


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- [x] Acesso a um computador com Python -> (Python 3.11.7)
- [x] Terminal Linux/Mac (ou WSL)
- [x] Docker e docker compose -> (Docker version 26.1.3) - (Docker Compose version v2.27.1)

## 🚀 Instalando API Brasilprev

```
$ cd pasta/onde/vc/guarda/seus/projetos
$ git git@github.com:evaristofm/api-brasilprev.git

```

próximo passo: no diretorio raiz do repositório executar:


```
$ docker compose up -d --build

```

próximo passo: execute as migraões do projeto usando docker compose + alembic


```
$ docker compose exec api prev alembic upgrade head

```

Cobertura de testes (ambiente linux)

```
$ ./tests.sh

```

![testes](https://github.com/evaristofm/api-brasilprev/assets/46290279/2d2632e9-6af2-48c6-bf11-078ddc6f9f20)


Acessando a documentação SWAGGER da API

```
http://localhost:8000/docs

```

![rotas_2](https://github.com/evaristofm/api-brasilprev/assets/46290279/c28434f2-593b-4c3f-a0d9-057a8daecac3)

Video demonstrando passo a passo dos endpoints:

https://drive.google.com/file/d/1VS7nUHmgm39KPteI1sHOhUVGTLG1qZ_1/view?usp=sharing
