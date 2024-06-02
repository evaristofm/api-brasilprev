import json
from fastapi import status

cliente_data = json.dumps({
    'nome': 'Joe Doe',
    'cpf': '11111111133',
    'email': 'joedoe@gmail.com',
    'genero': 'Masculino',
    'dataDeNascimento': '1992-05-31T13:58:44.777000Z',
    'rendaMensal': 2889.5})

produto_data = json.dumps({
    'nome': 'Brasilprev Longo Prazo 3',
    'susep': '15414900840201817',
    'expiracaoDeVenda': '2023-01-01T12:00:00.000Z',
    'valorMinimoAporteInicial': 1000.0,
    'valorMinimoAporteExtra': 100.0,
    'idadeDeEntrada': 18,
    'idadeDeSaida': 60,
    'carenciaInicialDeResgate': 60,
    'carenciaEntreResgates': 30
})


def test_cadastro_resgate_retorno_201(api_client):
    cliente_response = api_client.post('/cliente/', json=json.loads(cliente_data)).json()
    produto_response = api_client.post('/produto/', json=json.loads(produto_data)).json()

    plano_data = json.dumps({
        'idCliente': cliente_response.get('id'),
        'idProduto': produto_response.get('id'),
        'aporte': 15000,
        'dataDaContratacao': '2024-06-01T13:58:44.777000Z',
        'idadeDeAposentadoria': 60
    })
    plano_response = api_client.post('/plano/', json=json.loads(plano_data)).json()

    resgate_data = json.dumps({
        'idPlano': plano_response.get('id'),
        'valorResgate': 1000
    })

    resgate = api_client.post('/resgate/', json=json.loads(resgate_data))
    assert resgate.status_code == 201

