import json
from proyecto import procesar_inventario


def guardar_servidores():
    servidores, _ = procesar_inventario("inventario.txt")
    with open("lista_servidores.json", "w", encoding="utf-8") as f:
        json.dump(servidores, f, indent=4, ensure_ascii=False)


def leer_servidores():
    with open("lista_servidores.json", "r", encoding="utf-8") as f:
        return json.load(f)


def cargar_servidores():
    guardar_servidores()
    return leer_servidores()


if __name__ == "__main__":
    for s in cargar_servidores():
        print(s)
