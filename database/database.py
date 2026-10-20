import sqlite3

DATABASE = "database/zoo.db"

def get_connection():
    return sqlite3.connect(DATABASE)

# Criando as tabelas
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal TEXT NOT NULL,
            action TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()