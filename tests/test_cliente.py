import json
from fastapi import status


def test_consulta_retorno_get_clientes(api_client):
    response = api_client.get("/cliente/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_cadastro_cliente_retorno_id_e_status_code_201(api_client):
    data = json.dumps({
        'nome': 'Evaristo',
        'cpf': '10967581486',
        'email': 'evaristofm@gmail.com',
        'genero': 'Masculino',
        'dataDeNascimento': '1992-05-31T13:58:44.777000Z',
        'rendaMensal': 2889.5})
    
    response = api_client.post("/cliente/", json=json.loads(data))
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.json()

    