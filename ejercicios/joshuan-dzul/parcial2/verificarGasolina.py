"""
--- Programa de Control de Combustible ---
Este script determina si un vehículo puede circular 
basándose en la cantidad de litros disponibles.

1. Captura de datos:
olicitamos la entrada y la convertimos a float para permitir decimales.
"""
gasolina = float(input("Introduce los litros de gasolina: "))

"""
2. Lógica de decisión:
Evaluamos si el nivel de combustible es superior al umbral crítico (5 litros).
"""
if gasolina > 5:
    # Se ejecuta si la condición 'gasolina > 5' es verdadera (True).
    print("Puedes avanzar")
else:
    # Se ejecuta si la condición es falsa (False), es decir, 5 o menos.
    print("Necesitas gasolina")
