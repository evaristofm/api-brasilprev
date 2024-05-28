import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError

from prev.app import app
from prev.cli import create_cliente


os.environ["DUNDIE_DB__uri"] = "postgresql://postgres:postgres@db:5432/dundie_test"

@pytest.fixture(scope="function")
def api_client():
    return TestClient(app)


@pytest.fixture(scope="function")
def cria_cliente_1():
    try:
        create_cliente(
            nome="Elda Palumbo",
            cpf="48254720010",
            email="test1@gmail.com",
            genero="Feminino",
            rendamensal=2500.00)
    except IntegrityError:
        pass

# @pytest.fixture(scope="function")
# def cria_cliente_2():
#     try:
#         create_cliente(
#             nome="Pacifico Giordano",
#             cpf="58782727090",
#             email="test2@gmail.com",
#             genero="Masculino",
#             rendamensal=2500.00)
#     except IntegrityError:
#         pass

# @pytest.fixture(scope="function")
# def cria_cliente_1():
    try:
        create_cliente(
            nome="Sig. Avide Guerra",
            cpf="59514036000",
            email="test3@gmail.com",
            genero="Masculino",
            rendamensal=2500.00)
    except IntegrityError:
        pass