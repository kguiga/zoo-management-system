def salvar_atividade(texto):
    with open("atividades.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")


def ler_atividades():
    try:
        with open("atividades.txt", "r", encoding="utf-8") as arquivo:
            print(arquivo.read())

    except FileNotFoundError:
        print("Nenhum registro encontrado.")