# -----------------------------------------------
# Autor: Nancy Campos Basurto
# Proyecto: Registro y Análisis del Clima Semanal
# Paradigma: Programación Orientada a Objetos
# Conceptos aplicados: Encapsulamiento, Herencia, Polimorfismo
# -----------------------------------------------

# Clase base con método polimórfico
class RegistroClimaBase:
    def __init__(self, dia, temperatura):
        self.__dia = dia
        self.__temperatura = temperatura

    def obtener_dia(self):
        return self.__dia

    def obtener_temperatura(self):
        return self.__temperatura

    # Método polimórfico
    def mostrar_info(self):
        return f"{self.__dia}: {self.__temperatura} °C"

# Clase hija para temperaturas normales
class RegistroClimaNormal(RegistroClimaBase):
    def mostrar_info(self):
        return f"{self.obtener_dia()} (clima estable): {self.obtener_temperatura()} °C"

# Clase hija para temperaturas extremas (muy altas o muy bajas)
class RegistroClimaExtremo(RegistroClimaBase):
    def mostrar_info(self):
        return f"{self.obtener_dia()} ⚠️ ¡Temperatura extrema! → {self.obtener_temperatura()} °C"

# Clase que gestiona la semana completa
class SemanaClimatica:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, dia, temperatura):
        # Aplica polimorfismo según la temperatura
        if temperatura > 35 or temperatura < 5:
            registro = RegistroClimaExtremo(dia, temperatura)
        else:
            registro = RegistroClimaNormal(dia, temperatura)
        self.registros.append(registro)

    def ingresar_temperaturas_semana(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print("=== INGRESO DE TEMPERATURAS ===")
        for dia in dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para {dia}: "))
                    self.agregar_registro(dia, temp)
                    break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

    def calcular_promedio(self):
        if not self.registros:
            return 0.0
        suma = sum(reg.obtener_temperatura() for reg in self.registros)
        return suma / len(self.registros)

    def mostrar_resumen(self):
        print("\n=== RESUMEN SEMANAL DEL CLIMA ===")
        for registro in self.registros:
            print(registro.mostrar_info())
        print(f"\n🌡️ Promedio semanal: {self.calcular_promedio():.2f} °C")


# Función principal
def main():
    print("\n******** SISTEMA UNIVERSITARIO DE CLIMA SEMANAL ********\n")
    semana = SemanaClimatica()
    semana.ingresar_temperaturas_semana()
    semana.mostrar_resumen()
    print("\nGracias por utilizar el sistema.")

# Punto de entrada
if __name__ == "__main__":
    main()
