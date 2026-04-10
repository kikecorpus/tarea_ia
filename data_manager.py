import json
import os

FILE_PATH = "inventario.json"


def load_data():
    try:
        if not os.path.exists(FILE_PATH):
            return []

        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("⚠️ Archivo JSON corrupto. Reiniciando datos...")
        return []

    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return []


def save_data(data):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"Error al guardar datos: {e}")