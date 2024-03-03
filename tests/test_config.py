import os
import pytest


from app.config import Config


def test_config():
    app_config = Config()

    assert app_config.DB_DNS is not None
    assert isinstance(app_config.DB_DNS, str)
