from datetime import datetime
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo

from marshmallow import fields
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class Transacao:
    cliente_id: int
    tipo: str
    valor: int
    descricao: str
    realizada_em: datetime = field(metadata=config(
        encoder=lambda x: x.astimezone(ZoneInfo("America/Fortaleza")).isoformat(),
        decoder=datetime.fromisoformat,
        mm_field=fields.AwareDateTime(format='iso', default_timezone=ZoneInfo("America/Fortaleza"))
    ))  # type: ignore
    id_: int | None = None
