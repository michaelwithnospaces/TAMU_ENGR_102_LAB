# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-2
# Date: 15 SEPTEMBER 2023

import math

# beginning
print(f'This program calculates the applied force given mass and acceleration')
mass = float(input('Please enter the mass (kg): '))
acceleration = float(input('Please enter the acceleration (m/s^2): '))
force = mass * acceleration

print(f"Force is {force:.1f} N")

print('This program calculates the wavelength given distance and angle')
distance = float(input('Please enter the distance (nm): '))
scattering_angle = float(input('Please enter the angle (degrees): '))
scattering_angle_radians = math.radians(scattering_angle)
order = 1
wavelength = 2 * distance * math.sin(scattering_angle_radians) / order

print(f"Wavelength is {wavelength:.4f} nm")

print('This program calculates how much Radon-222 is left given time and initial amount')
time = float(input('Please enter the time (days): '))
initial_amount = float(input('Please enter the initial amount (g): '))
half_life = 3.8
radon = initial_amount * math.pow(2, -time / half_life)

print(f"Radon-222 left is {radon:.2f} g")

print('This program calculates the pressure given moles, volume, and temperature')
moles = float(input('Please enter the number of moles: '))
volume = float(input('Please enter the volume (m^3): '))
temperature = float(input('Please enter the temperature (K): '))
gas_constant = 8.314
pressure = (moles * gas_constant * temperature) / volume
pressure *= .001

print(f"Pressure is {pressure:.0f} kPa")
