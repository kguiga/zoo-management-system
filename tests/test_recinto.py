from src.recinto import Recinto

def test_criar_recinto():
    recinto = Recinto("Gaiola")

    assert  recinto.nome == "Gaiola"


def test_limpar_recinto():
    recinto = Recinto("Gaiola")

    assert recinto.limpar() == "Recinto Gaiola foi limpo"