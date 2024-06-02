import json
from fastapi import status


def test_consulta_produto_retorno_status_200(api_client):
    response = api_client.get("/produto/")
    assert response.status_code == status.HTTP_200_OK


def test_cadastro_produto_retorno_status_201(api_client):
    data = json.dumps({
        'nome': 'Brasilprev Longo Prazo',
        'susep': '15414900840201817',
        'expiracaoDeVenda': '2026-01-01T12:00:00.000Z',
        'valorMinimoAporteInicial': 1000.0,
        'valorMinimoAporteExtra': 100.0,
        'idadeDeEntrada': 18,
        'idadeDeSaida': 60,
        'carenciaInicialDeResgate': 60,
        'carenciaEntreResgates': 30
    })

    response = api_client.post("/produto/", json=json.loads(data))
    assert response.status_code == status.HTTP_201_CREATED
    

def test_cadastro_produto_retorno_id(api_client):
    data = json.dumps({
        'nome': 'Brasilprev Longo Prazo',
        'susep': '15414900840201817',
        'expiracaoDeVenda': '2026-01-01T12:00:00.000Z',
        'valorMinimoAporteInicial': 1000.0,
        'valorMinimoAporteExtra': 100.0,
        'idadeDeEntrada': 18,
        'idadeDeSaida': 60,
        'carenciaInicialDeResgate': 60,
        'carenciaEntreResgates': 30
    })

    response = api_client.post("/produto/", json=json.loads(data))
    assert 'id' in response.json()