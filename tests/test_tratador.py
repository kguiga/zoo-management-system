from src.tratador import Tratador
from src.animal import Leao, Macaco, Elefante
from src.recinto import Recinto

def test_criar_tratador():
    tratador = Tratador("Karina")

    assert tratador.nome == "Karina"


def test_banho_sol():
    leao = Leao("Simba")
    tratador = Tratador("Karina")

    assert tratador.banho_sol(leao) == "Simba tomou banho de sol"


def test_alimentar_animal():
    tratador = Tratador("Karina")
    macaco = Macaco("Caco")

    assert tratador.alimentar_animal(macaco) == "Caco foi alimentado com Frutas"


def test_tratar_animal():
    tratador = Tratador("Karina")
    elefante = Elefante("Dumbo")

    assert tratador.tratar_animal(elefante) == "Dumbo recebeu banho medicinal"


def test_limpar_recinto():
    tratador = Tratador("Karina")
    recinto = Recinto("Aquario")

    assert tratador.limpar_recinto(recinto) == "Recinto Aquario foi limpo"