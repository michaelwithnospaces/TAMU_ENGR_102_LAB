# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: MICHAEL NGUYEN
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Section: 536
# Assignment: LAB-3
# Date: 15 SEPTEMBER 2023

def linear_interpolation(t, t0, x0, y0, z0, t2, x2, y2, z2): #no return function
    x1 = ((x2 - x0) / (t2 - t0)) * (t - t0) + x0
    y1 = ((y2 - y0) / (t2 - t0)) * (t - t0) + y0
    z1 = ((z2 - z0) / (t2 - t0)) * (t - t0) + z0

    print(f'At time {t:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})')


def main():
    t0 = float(input('Enter time 1: '))
    x0 = float(input('Enter the x position of the object at time 1: '))
    y0 = float(input('Enter the y position of the object at time 1: '))
    z0 = float(input('Enter the z position of the object at time 1: '))

    t2 = float(input('Enter time 2: '))
    x2 = float(input('Enter the x position of the object at time 2: '))
    y2 = float(input('Enter the y position of the object at time 2: '))
    z2 = float(input('Enter the z position of the object at time 2: '))

    increment = (t2 - t0) / 4.0
    t = t0

    linear_interpolation(t, t0, x0, y0, z0, t2, x2, y2, z2)
    t += increment
    linear_interpolation(t, t0, x0, y0, z0, t2, x2, y2, z2)
    t += increment
    linear_interpolation(t, t0, x0, y0, z0, t2, x2, y2, z2)
    t += increment
    linear_interpolation(t, t0, x0, y0, z0, t2, x2, y2, z2)
    t += increment
    linear_interpolation(t, t0, x0, y0, z0, t2, x2, y2, z2)


if __name__ == "__main__":
    main()
