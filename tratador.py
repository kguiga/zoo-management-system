class Tratador:
    def __init__(self, nome):
        self.nome = nome

    def alimentar_animal(self, animal):
        return animal.alimentar()

    def tratar_animal(self, animal):
        return animal.tratar()

    def limpar_recinto(self, recinto):
        return recinto.limpar()

    def banho_sol(self, animal):
        return f"{animal.nome} tomou banho de sol"