import numpy as np # Importar la librería numpy para trabajar con las matrices

# Definición de las matrices A, B y C
A = np.array([
    [7, 2, 4, -5, 2],
    [-4, -4, 3, 6, 0],
    [5, 6, 97, 8, 4],
    [13, 0, 30, 3, 3]
])

B = np.array([
    [-2, 5, 0, -15, -1],
    [7, 6, 8, -20, 0],
    [3, 0, 0, 0, 10],
    [2, -5, -2, 10, 9]
])

C = np.array([
    [5, -8, 0, -20, 1],
    [-2, -4, -3, 5, 2],
    [-5, 0, -4, 50, 24],
    [0, 90, -5, -3, 4]
])

# Imprimir las dimensiones de las matrices A, B y C para verificar que son iguales en tamaño y que es posible resolver el sistema
print("Dimensión de cada matriz:") 
print(f"A: {A.shape}") 
print(f"B: {B.shape}")
print(f"C: {C.shape}")

# Parte a): 3X - B = 2A - C
# Despejamos X: 3X = 2A - C + B
#               X = (2A - C + B) * (1/3)

def resolver_parte_a(): # función para resolver la parte a)
    
    # Calculamos el lado derecho de la ecuación
    lado_derecho = 2 * A - C + B
    
    # Multiplicamos por 1/3 para obtener X 
    X = lado_derecho * (1/3)
    
    # Verificamos la solución usando la ecuación original y el valor de la matriz X
    # 3X - B = 2A - C
    verificacion = 3 * X - B # Calculamos el lado izquierdo de la ecuación
    esperado = 2 * A - C # Calculamos el lado derecho de la ecuación
    
    # Verificamos la solución
    return X, verificacion, esperado 

# Parte b): 6A + 4X = B + 2C + 6X
# Despejamos X: -B + 6A + 4X = -2C + 6X
#               -2C - B + 6A + 4X = 6X
#               -2C - B + 6A = 6X - 4X
#               .2C - B + 6A = 2X
# Por lo tanto: X = (-2C - B + 6A) * (1/2)

def resolver_parte_b():
    # Calculamos el lado derecho de la ecuación
    lado_derecho = -2 * C - B + 6 * A
    
    # Multiplicamos por 1/2 para obtener X
    X = lado_derecho * (1/2)
    
    # Verificamos la solución usando la ecuación original y el valor de la matriz X
    # 6A + 4X = B + 2C + 6X
    verificacion = 6 * A + 4 * X # Calculamos el lado izquierdo de la ecuación
    esperado = B + 2 * C + 6 * X # Calculamos el lado derecho de la ecuación
    
    # Verificamos la solución
    return X, verificacion, esperado

# Resolver parte a)
# Llama a la función resolver_parte_a() y almacena las respuestas en las variables X_a, verif_a y esperado_a (X, verificación y esperado respectivamente)
X_a, verif_a, esperado_a = resolver_parte_a() 
print("\n--- Solución parte a) ---") 
print("X = ") 
print(X_a) # Imprime la solución de la parte a)

# Verificar solución parte a)
print("\nVerificación parte a):")
print("3X - B = ")
print(verif_a) # Imprime el lado izquierdo de la ecuación
print("\n2A - C = ")
print(esperado_a) # Imprime el lado derecho de la ecuación
print("\n¿Son iguales? ", np.allclose(verif_a, esperado_a)) # Verifica si el lado izquierdo y derecho son iguales usando np.allclose() 

# Resolver parte b)
X_b, verif_b, esperado_b = resolver_parte_b() # Llama a la función resolver_parte_b() y almacena las respuestas en las variables X_b, verif_b y esperado_b (X, verificación y esperado respectivamente)
print("\n--- Solución parte b) ---") 
print("X = ")
print(X_b) # Imprime la solución de la parte b)

# Verificar solución parte b)
print("\nVerificación parte b):")
print("6A + 4X = ")
print(verif_b) # Imprime el lado izquierdo de la ecuación
print("\nB + 2C + 6X = ")
print(esperado_b) # Imprime el lado derecho de la ecuación
print("\n¿Son iguales? ", np.allclose(verif_b, esperado_b)) # Verifica si el lado izquierdo y derecho son iguales usando np.allclose()

# Se usa np.allclose() para verificar si dos matrices son iguales evitando errores de redondeo
# Fin del programa 