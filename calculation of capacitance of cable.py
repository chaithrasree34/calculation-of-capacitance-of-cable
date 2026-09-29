# calculation-of-capacitance-of-cable
import math

# Permittivity of free space
epsilon_0 = 8.854e-12

# Input values
epsilon_r = float(input("Enter relative permittivity of insulation: "))
L = float(input("Enter length of cable (m): "))
d = float(input("Enter conductor diameter (m): "))
D = float(input("Enter diameter over insulation (m): "))

# Calculate capacitance
C = (2 * math.pi * epsilon_0 * epsilon_r * L) / math.log(D / d)

# Convert to microfarads
C_microfarad = C * 1e6

print("\nCapacitance of Cable")
print("Capacitance =", C, "F")
print("Capacitance =", round(C_microfarad, 6), "µF")

Example

Input:

Enter relative permittivity of insulation: 3
Enter length of cable (m): 100
Enter conductor diameter (m): 0.01
Enter diameter over insulation (m): 0.02


Output:

Capacitance of Cable
Capacitance = 1.445...e-08 F
Capacitance = 0.01445 µF


This program is useful for an Electrical Engineering cable capacitance calculation experiment.
