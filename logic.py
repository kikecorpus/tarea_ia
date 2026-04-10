from data_manager import load_data, save_data

VALID_STATES = ["Excelente", "Dañado", "En Mantenimiento"]


def register_computer(id, marca, modelo):
    data = load_data()

    for comp in data:
        if comp["id"] == id:
            return "❌ El computador ya existe."

    new_computer = {
        "id": id,
        "marca": marca,
        "modelo": modelo,
        "estado": "Excelente",
        "asignado_a": None
    }

    data.append(new_computer)
    save_data(data)

    return "✅ Computador registrado."


def assign_computer(id, camper):
    data = load_data()

    for comp in data:
        if comp["id"] == id:
            if comp["asignado_a"] is not None:
                return "❌ Ya está asignado."

            comp["asignado_a"] = camper
            save_data(data)
            return "✅ Computador asignado."

    return "❌ Computador no encontrado."


def update_status(id, estado):
    if estado not in VALID_STATES:
        return "❌ Estado inválido."

    data = load_data()

    for comp in data:
        if comp["id"] == id:
            comp["estado"] = estado
            save_data(data)
            return "✅ Estado actualizado."

    return "❌ Computador no encontrado."


def view_inventory():
    data = load_data()

    if not data:
        return "📭 Inventario vacío."

    result = "\n--- INVENTARIO ---\n"

    for comp in data:
        result += (
            f"ID: {comp['id']} | "
            f"{comp['marca']} {comp['modelo']} | "
            f"Estado: {comp['estado']} | "
            f"Asignado a: {comp['asignado_a']}\n"
        )

    return result