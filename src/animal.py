class Animal:
    def __init__(self, nome, especie, alimentacao):
        self.nome = nome
        self.especie = especie
        self.alimentacao = alimentacao

    def alimentar(self):
        return f"{self.nome} foi alimentado com {self.alimentacao}"

    def tratar(self):
        return f"{self.nome} recebeu tratamento"


class Leao(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Leão", "Carne")

    def tratar(self):
        return f"{self.nome} recebeu tratamento veterinário especial"


class Macaco(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Macaco", "Frutas")

    def tratar(self):
        return f"{self.nome} recebeu suplementação alimentar"


class Elefante(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Elefante", "Capim")

    def tratar(self):
        return f"{self.nome} recebeu banho medicinal"