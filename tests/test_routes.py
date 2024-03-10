from app.main import app
from starlette.testclient import TestClient


def test_retrieve_transacoes(test_app, session):
    client = TestClient(test_app)

    response = client.get("/clientes/1/transacoes")

    assert response is not None
    assert response.status_code == 200
    print(response.json())
