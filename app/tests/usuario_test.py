import pytest
from app.models.usuario import Usuario


def test_nome_invalido():
    with pytest.raises(TypeError, match="Nome não pode estar vazio e deve ser um texto!"):
        Usuario(3, "LPL@gmail.com", "123") or Usuario("", "LPL@gmail.com", "123")

def test_email_invalido():
    with pytest.raises(TypeError, match="Email não pode estar vazio e deve ser um texto!"):
        Usuario("LPL", 3, "123") or Usuario("LPL", "", "123")

def test_senha_invalida():
    with pytest.raises(TypeError, match="Senha não pode estar vazia e deve ser um texto!"):
        Usuario("LPL", "LPL@gmail.com", 123) or Usuario("LPL", "LPL@gmail.com", "")