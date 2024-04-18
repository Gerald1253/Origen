def calcular_mcd(a, b):
    """
    Función para calcular el máximo común divisor (MCD) utilizando el algoritmo de Euclides.
    """
    while b:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    """
    Función para calcular el mínimo común múltiplo (MCM) utilizando la relación MCM(a, b) = (a * b) / MCD(a, b)
    """
    return (a * b) // calcular_mcd(a, b)

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular el MCD y el MCM
mcd = calcular_mcd(num1, num2)
mcm = calcular_mcm(num1, num2)

# Mostrar los resultados
print("El MCD de", num1, "y", num2, "es:", mcd)
print("El MCM de", num1, "y", num2, "es:", mcm)
