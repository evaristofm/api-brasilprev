import json
import pytest

@pytest.mark.order(1)
def test_create_cliente(api_client):
  data = {
        "cpf": "string",
        "nome": "string",
        "email": "string",
        "dataDeNascimento": "2024-05-28T04:00:12.271Z",
        "genero": "string",
        "rendaMensal": 0
  }
  cliente = api_client.post("/cliente/", json=json.dumps(data))
  assert cliente.status_code == 201

  
