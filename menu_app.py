# menu_app.py

def agregar_compra(compras):
    try:
        monto_compra = float(input("Ingrese el monto de la compra: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    compras.append(monto_compra)
    print(f"Compra ${monto_compra:.2f} agregada correctamente.")


def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, monto in enumerate(compras, 1):
            print(f"{i}. ${monto:.2f}")


def mostrar_total(compras):
    total_gastado = sum(compras)
    print(f"Total gastado: ${total_gastado:.2f}")


def main():
    compras = []

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
