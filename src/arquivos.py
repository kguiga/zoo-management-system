from database.database import get_connection


def salvar_atividade(texto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO activities (description) VALUES (?)",
        (texto,)
    )

    conn.commit()
    conn.close()


def ler_atividades():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT description FROM activities"
    )

    atividades = cursor.fetchall()

    if not atividades:
        print("Nenhum registro encontrado.")
    else:
        for atividade in atividades:
            print(atividade[0])

    conn.close()