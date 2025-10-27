from incertidumbre_probabilidad import ejecutar_probabilidad
from funciones_pertenencia import ejecutar_pertenencia
from defuzificacion_centroide import ejecutar_defuzificacion


def main():
    print("\n==============================")
    print(" PRÁCTICA 3 – LÓGICA DIFUSA ")
    print("==============================\n")

    print("▶ 1. INCERTIDUMBRE Y PROBABILIDAD")
    ejecutar_probabilidad()

    print("\n▶ 2. FUNCIONES DE PERTENENCIA")
    ejecutar_pertenencia()

    print("\n▶ 3. DEFUZIFICACIÓN (MÉTODO DEL CENTROIDE)")
    ejecutar_defuzificacion()

    print("\n✅ Ejecución completa. Práctica finalizada.\n")


if __name__ == "__main__":
    main()
