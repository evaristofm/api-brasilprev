#!/usr/bin/bash

# Arquivos na raiz
touch setup.py
touch {pyproject,settings,.secrets}.toml
touch {requirements,MANIFEST}.in
touch Dockerfile.dev docker-compose.yaml

# Imagem do banco de dados
mkdir postgres
touch postgres/{Dockerfile,create-databases.sh}

# Aplicação
mkdir -p prev/{models,routes}
touch prev/default.toml
touch prev/{__init__,cli,app,auth,db,security,config}.py
touch prev/models/{__init__,account,user}.py
touch prev/routes/{__init__,auth,account,user}.py

# Testes
touch test.sh
mkdir tests
touch tests/{__init__,conftest,test_api}.py
