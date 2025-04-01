# Start
#
# Display a menu to the user:
#
# Find roots of a cubic equation
#
# Find roots of a quartic equation
#
# Find roots of a quadratic equation
#
# Get the user’s choice
#
# Based on choice:
#
# Cubic: Request coefficients A, B, C, D; solve using numpy.roots()
#
# Quartic: Request coefficients A, B, C, D, E; solve using numpy.roots()
#
# Quadratic: Request coefficients A, B, C; solve using quadratic formula
#
# Display the roots
#
# End

import numpy as np
import cmath

print("Select the type of equation:")
print("1. Cubic Equation (Ax³ + Bx² + Cx + D = 0)")
print("2. Quartic Equation (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
print("3. Quadratic Equation (Ax² + Bx + C = 0)")

choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))
    roots = np.roots([A, B, C, D])
    print(f"Roots of the cubic equation: {roots}")

elif choice == 2:
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))
    E = float(input("Enter coefficient E: "))
    roots = np.roots([A, B, C, D, E])
    print(f"Roots of the quartic equation: {roots}")

elif choice == 3:
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    discriminant = (B**2) - (4*A*C)
    root1 = (-B + cmath.sqrt(discriminant)) / (2*A)
    root2 = (-B - cmath.sqrt(discriminant)) / (2*A)
    print(f"Roots of the quadratic equation: {root1} and {root2}")

else:
    print("Invalid choice. Please run again and select 1, 2, or 3.")




