from datetime import datetime

from app.models import Transacao


def test_transacao_instantiation(transacao):
    assert transacao is not None
    assert transacao.id_ is None


def test_transacao_to_json(transacao):
    assert transacao.to_json() == (
        '{"cliente_id": 1, "tipo": "c", "valor": 1100, "descricao":'
        ' "testando", "realizada_em": "2021-02-02T11:15:03-03:00", '
        '"id_": null}'
    )
