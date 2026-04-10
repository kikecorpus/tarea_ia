import os
import json
import unittest
from data_manager import load_data, save_data
from logic import register_computer, assign_computer, update_status, view_inventory

class TestDataManager(unittest.TestCase):
    def setUp(self):
        # Limpiar archivo antes de cada prueba
        if os.path.exists("inventario.json"):
            os.remove("inventario.json")

    def test_load_data_no_file(self):
        result = load_data()
        self.assertEqual(result, [])

    def test_save_and_load_data(self):
        data = [{"id": "PC001", "marca": "Dell", "modelo": "Inspiron", "estado": "Excelente", "asignado_a": None}]
        save_data(data)
        result = load_data()
        self.assertEqual(result, data)

    def test_load_corrupt_json(self):
        with open("inventario.json", "w") as f:
            f.write('{"invalid": json')
        result = load_data()
        self.assertEqual(result, [])

class TestLogic(unittest.TestCase):
    def setUp(self):
        if os.path.exists("inventario.json"):
            os.remove("inventario.json")

    def test_register_computer(self):
        result = register_computer("PC001", "Dell", "Inspiron")
        self.assertEqual(result, "✅ Computador registrado.")
        data = load_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], "PC001")

    def test_register_duplicate(self):
        register_computer("PC001", "Dell", "Inspiron")
        result = register_computer("PC001", "HP", "Pavilion")
        self.assertEqual(result, "❌ El computador ya existe.")

    def test_assign_computer(self):
        register_computer("PC001", "Dell", "Inspiron")
        result = assign_computer("PC001", "Juan Pérez")
        self.assertEqual(result, "✅ Computador asignado.")
        data = load_data()
        self.assertEqual(data[0]["asignado_a"], "Juan Pérez")

    def test_assign_already_assigned(self):
        register_computer("PC001", "Dell", "Inspiron")
        assign_computer("PC001", "Juan Pérez")
        result = assign_computer("PC001", "Ana López")
        self.assertEqual(result, "❌ Ya está asignado.")

    def test_update_status(self):
        register_computer("PC001", "Dell", "Inspiron")
        result = update_status("PC001", "Dañado")
        self.assertEqual(result, "✅ Estado actualizado.")
        data = load_data()
        self.assertEqual(data[0]["estado"], "Dañado")

    def test_update_invalid_status(self):
        register_computer("PC001", "Dell", "Inspiron")
        result = update_status("PC001", "Roto")
        self.assertEqual(result, "❌ Estado inválido.")

    def test_view_inventory_empty(self):
        result = view_inventory()
        self.assertEqual(result, "📭 Inventario vacío.")

    def test_view_inventory_with_data(self):
        register_computer("PC001", "Dell", "Inspiron")
        result = view_inventory()
        self.assertIn("PC001", result)
        self.assertIn("Dell Inspiron", result)

class TestInventarioJSON(unittest.TestCase):
    def setUp(self):
        if os.path.exists("inventario.json"):
            os.remove("inventario.json")

    def test_valid_json(self):
        data = [{"id": "PC001", "marca": "Dell", "modelo": "Inspiron", "estado": "Excelente", "asignado_a": None}]
        save_data(data)
        with open("inventario.json", "r") as f:
            content = f.read()
        try:
            parsed = json.loads(content)
            self.assertIsInstance(parsed, list)
        except json.JSONDecodeError:
            self.fail("JSON inválido")

    def test_empty_json(self):
        save_data([])
        with open("inventario.json", "r") as f:
            content = f.read()
        parsed = json.loads(content)
        self.assertEqual(parsed, [])

if __name__ == "__main__":
    # Para main.py, como es interactivo, no se automatiza fácilmente, pero podemos probar importando
    print("Ejecutando pruebas QA automatizadas...")
    unittest.main(verbosity=2)