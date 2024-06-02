import json
from fastapi import status

CLIENTE_DATA = json.dumps({
        'nome': 'Julio',
        'cpf': '45203694010',
        'email': 'julio@gmail.com',
        'genero': 'Masculino',
        'dataDeNascimento': '1992-05-31T13:58:44.777000Z',
        'rendaMensal': 2889.5})

PRODUTO_DATA = json.dumps({
        'nome': 'Brasilprev Longo Prazo 2',
        'susep': '15414900840201817',
        'expiracaoDeVenda': '2026-01-01T12:00:00.000Z',
        'valorMinimoAporteInicial': 1000.0,
        'valorMinimoAporteExtra': 100.0,
        'idadeDeEntrada': 18,
        'idadeDeSaida': 60,
        'carenciaInicialDeResgate': 60,
        'carenciaEntreResgates': 30
    })


def test_cadastro_plano_retorno_id_status_code_201(api_client):
    cliente_data = json.dumps({
        'nome': 'Julio',
        'cpf': '11111111111',
        'email': 'julio21@gmail.com',
        'genero': 'Masculino',
        'dataDeNascimento': '1990-05-31T13:58:44.777000Z',
        'rendaMensal': 2889.5})
    
    produto_data = json.dumps({
        'nome': 'Brasilprev Longo Prazo 2',
        'susep': '15414900840201817',
        'expiracaoDeVenda': '2026-01-01T12:00:00.000Z',
        'valorMinimoAporteInicial': 1000.0,
        'valorMinimoAporteExtra': 100.0,
        'idadeDeEntrada': 18,
        'idadeDeSaida': 60,
        'carenciaInicialDeResgate': 60,
        'carenciaEntreResgates': 30
    })
    cliente_response = api_client.post('/cliente/', json=json.loads(cliente_data)).json()
    produto_response = api_client.post('/produto/', json=json.loads(produto_data)).json()

    plano_data = json.dumps({
        'idCliente': cliente_response.get('id'),
        'idProduto': produto_response.get('id'),
        'aporte': float(15000),
        'dataDaContratacao': '2023-01-01T13:58:44.777000Z',
        'idadeDeAposentadoria': 60
    })

    plano_response = api_client.post('/plano/', json=json.loads(plano_data))

    assert plano_response.status_code == status.HTTP_201_CREATED
    assert 'id' in plano_response.json()

