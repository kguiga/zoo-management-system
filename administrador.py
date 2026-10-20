class Administrador:
    def __init__(self):
        self.registros = []

    def registrar(self, tratador, atividade):
        self.registros.append(
            f"Tratador: {tratador} | Atividade: {atividade}"
        )

    def exibir_relatorio(self):
        print("\n===== RELATÓRIO =====")

        for registro in self.registros:
            print(registro)

        print(f"\nTotal de atividades: {len(self.registros)}")