# Encuesta y formulario de datos.

personas = []

while True:
    print("\nMenú:")
    print("a. Agregar una persona")
    print("b. Mostrar información personal de una persona")
    print("q. Salir")

    opcion = input("Seleccione una opción: ").lower()

    if opcion == "a":
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        fecha_nacimiento = input("Fecha de Nacimiento: ")
        correo = input("Correo: ")
        ciudad_residencia = input("Ciudad de Residencia: ")
        ciudad_origen = input("Ciudad de Origen: ")

        artista = input("Artista de la canción favorita: ")
        titulo = input("Título de la canción favorita: ")
        cancion_favorita = f"{artista} - {titulo}"

        persona = {
            "Nombre": nombre,
            "Cédula": cedula,
            "Fecha de Nacimiento": fecha_nacimiento,
            "Correo": correo,
            "Ciudad de Residencia": ciudad_residencia,
            "Ciudad de Origen": ciudad_origen,
            "Canción Favorita": cancion_favorita
        }

        personas.append(persona)
        print("Persona agregada con éxito.")

    elif opcion == "b":
        if personas:
            for i, persona in enumerate(personas):
                print(f"\nInformación de la persona:")
                for clave, valor in persona.items():
                    if clave == "Canción Favorita":
                        print(f"{clave}: {valor}")
                    else:
                        print(f"{clave}: {valor}")
        else:
            print("No hay personas registradas.")

    elif opcion == "q":
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")