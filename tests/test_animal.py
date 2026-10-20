from src.animal import *


def test_animal_generico():
    animal = Animal("Bidu", "Cachorro", "Ração")

    assert animal.nome == "Bidu"
    assert animal.especie == "Cachorro"
    assert animal.alimentacao == "Ração"


def test_alimentar_animal():
    animal = Animal("Bidu", "Cachorro", "Ração")

    assert animal.alimentar() == "Bidu foi alimentado com Ração"


def test_tratar_animal():
    animal = Animal("Bidu", "Cachorro", "Ração")

    assert animal.tratar() == "Bidu recebeu tratamento"


def test_leao():
    leao = Leao("Simba")

    assert leao.especie == "Leão"
    assert leao.alimentacao == "Carne"


def test_tratar_leao():
    leao = Leao("Simba")

    assert leao.tratar() == "Simba recebeu tratamento veterinário especial"


def test_macaco():
    macaco = Macaco("George")

    assert macaco.especie == "Macaco"
    assert macaco.alimentacao == "Frutas"


def test_tratar_macaco():
    macaco = Macaco("George")

    assert macaco.tratar() == "George recebeu suplementação alimentar"


def test_elefante():
    elefante = Elefante("Dumbo")

    assert elefante.especie == "Elefante"
    assert elefante.alimentacao == "Capim"


def test_tratar_elefante():
    elefante = Elefante("Dumbo")

    assert elefante.tratar() == "Dumbo recebeu banho medicinal"