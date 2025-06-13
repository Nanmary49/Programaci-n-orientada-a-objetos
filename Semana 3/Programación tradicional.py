# -----------------------------------------------
# Autor: Nancy Campos Basurto
# Proyecto: Cálculo del Promedio Semanal de Temperaturas
# Enfoque: Programación Tradicional con funciones estructuradas
# -----------------------------------------------

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas de los 7 días de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese la temperatura promedio de cada día de la semana:")
    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio_semanal(lista_temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el promedio como un número flotante.
    """
    suma_total = sum(lista_temperaturas)
    promedio = suma_total / len(lista_temperaturas)
    return promedio


# Función principal que organiza la ejecución del programa
def ejecutar_programa():
    """
    Controla el flujo general del programa.
    """
    print("\n===== SISTEMA DE REGISTRO DE TEMPERATURAS SEMANALES =====\n")

    temperaturas_semana = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas_semana)

    print("\n>>> Resultados del análisis semanal:")
    print(f"Temperaturas ingresadas: {temperaturas_semana}")
    print(f"Promedio semanal de temperatura: {promedio:.2f} °C")
    print("\nGracias por utilizar el sistema.")


# Llamada al programa principal
ejecutar_programa()
