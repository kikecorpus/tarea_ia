from logic import (
    register_computer,
    assign_computer,
    update_status,
    view_inventory
)


def menu():
    print("\n===== SISTEMA INVENTARIO CAMPUSLANDS =====")
    print("1. Registrar computador")
    print("2. Asignar computador")
    print("3. Ver inventario")
    print("4. Actualizar estado")
    print("5. Salir")


def main():
    while True:
        menu()
        option = input("Seleccione una opción: ")

        if option == "1":
            id = input("ID: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            print(register_computer(id, marca, modelo))

        elif option == "2":
            id = input("ID del computador: ")
            camper = input("Nombre del camper: ")
            print(assign_computer(id, camper))

        elif option == "3":
            print(view_inventory())

        elif option == "4":
            id = input("ID del computador: ")
            estado = input("Estado (Excelente/Dañado/En Mantenimiento): ")
            print(update_status(id, estado))

        elif option == "5":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()