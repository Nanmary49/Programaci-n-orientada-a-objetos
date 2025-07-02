 Programa para calcular el Índice de Masa Corporal (IMC) de una persona
# El usuario ingresa su nombre, peso y altura.
# El programa calcula el IMC y determina si está en un rango saludable.
# Utiliza varios tipos de datos: string, float, integer, boolean.

def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """
    Calcula el índice de masa corporal (IMC).

    Fórmula: IMC = peso (kg) / altura² (m²)
    """
    return peso_kg / (altura_m ** 2)


# Solicitar información al usuario
nombre_usuario: str = input("Ingrese su nombre: ")
edad: int = int(input("Ingrese su edad: "))
peso: float = float(input("Ingrese su peso en kilogramos: "))
altura: float = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc: float = calcular_imc(peso, altura)

# Evaluar si el IMC es saludable
imc_saludable: bool = 18.5 <= imc <= 24.9

# Mostrar resultados
print(f"\nHola {nombre_usuario}, estos son tus resultados:")
print(f"Edad: {edad} años")
print(f"Tu IMC es: {imc:.2f}")

if imc_saludable:
    print("¡Tu IMC está en un rango saludable! ✅")
else:
    print("Tu IMC está fuera del rango saludable. ⚠️")


# Correción al commit anterior este archivo pertenece a la seman cinco