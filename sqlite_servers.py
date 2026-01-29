import sqlite3
from servers_json import cargar_servidores

DB = "servidores.db"

def crear_db(nombre_db):
    with sqlite3.connect(nombre_db) as conn:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS Servidores")
        c.execute("""
            CREATE TABLE Servidores (
                nombre TEXT PRIMARY KEY,
                ip TEXT,
                sistema TEXT,
                ubicacion TEXT,
                responsable TEXT
            )
        """)


def insertar_datos():
    servidores = cargar_servidores()
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        for s in servidores:
            c.execute("""
                INSERT OR REPLACE INTO Servidores
                VALUES (?, ?, ?, ?, ?)
            """, tuple(s.values()))


def consultar(nombre):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Servidores WHERE nombre = ?", (nombre,))
        return c.fetchone()


def gestionar_servidores():
    while True:
        print("1-Crear BDD  2-Insertar Datos  3-Consultar  4-Salir")
        op = input("> ")

        if op == "1":
            crear_db(DB)
        elif op == "2":
            insertar_datos()
        elif op == "3":
            nombre = input("nombre del servidor: ")
            r = consultar(nombre)
            print(r if r else "servidor no existe")
        elif op == "4":
            break
        else:
            print("opcion incorrecta")


if __name__ == "__main__":
    gestionar_servidores()
