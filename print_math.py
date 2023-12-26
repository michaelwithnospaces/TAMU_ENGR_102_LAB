# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-1
# Date: 08 AUGUST 2023
#

import math

mass = 27 #kg
acceleration = 1.5 #m/s^2
force = mass * acceleration

distance = 0.025 #nm
scattering_angle = 35 #degrees
scattering_angle_radians = math.radians(scattering_angle)
order = 1
wavelength = 2 * distance * math.sin(scattering_angle_radians) / order

time = 5 #days
initial_amount = 27 #g
half_life = 3.8 #days
radon = initial_amount * math.pow(2, -(time) / half_life)

moles = 5
volume = 0.27 #m^3
temperature = 415 #k
gas_constant = 8.314 #m^3Pa/K·mol
pressure = (moles * gas_constant * temperature) / volume
pressure *= .001 #conversion

print(f"Force is {force} N")
print(f"Wavelength is {wavelength} nm")
print(f"Radon-222 left is {radon} g")
print(f"Pressure is {pressure} kPa")
