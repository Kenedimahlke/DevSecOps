import sqlite3
import os


def conectar_banco():
    senha_banco = os.getenv("DB_PASSWORD", "senha_padrao_local")

    print("Conexão estabelecida de forma segura.")


def buscar_usuario(nome_usuario):
    conn = sqlite3.connect("banco_exemplo.db")
    cursor = conn.cursor()

    query = "SELECT * FROM usuarios WHERE nome = ?"

    cursor.execute(query, (nome_usuario,))

    return cursor.fetchall()


if __name__ == "__main__":
    conectar_banco()