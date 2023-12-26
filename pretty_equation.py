# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-4
# Date: 03 OCTOBER 2023


def get_coeff(letter):
    coeff = int(input(f'Please enter the coefficient {letter}: '))
    return coeff


def get_sign(number):
    if number < 0:
        return '-'
    elif number > 0:
        return '+'
    else:
        return ''


def main():
    coeff_a = get_coeff('A')
    sign_a = get_sign(coeff_a)
    coeff_b = get_coeff('B')
    sign_b = get_sign(coeff_b)
    coeff_c = get_coeff('C')
    sign_c = get_sign(coeff_c)

    if not (coeff_a == 0 and coeff_b == 0 and coeff_c == 0):
        print(f'The quadratic equation is ', end='')
    else:
        print(f'There is no existing equation.')

    # coefficient a line
    if coeff_a != 0:
        print(f'{"- " if coeff_a < 0 else ""}{abs(coeff_a) if (abs(coeff_a) != 1) else ""}x^2', end='')

    # coefficient b line
    if coeff_b != 0:
        if coeff_a != 0:
            print(f' {sign_b} {abs(coeff_b) if abs(coeff_b) != 1 else ""}x', end='')
        else:
            print(f'{sign_b if (coeff_b < 0) else ""}{abs(coeff_b) if abs(coeff_b) != 1 else ""}x', end='')

    # coefficient c line

    if coeff_a == 0 and coeff_b == 0:
        print(coeff_c, end='')
    elif coeff_c != 0:
        print(f' {sign_c} {abs(coeff_c)}', end='')

    # final print statement
    if coeff_a == 0 and coeff_b == 0:
            print(' and does not equal 0')
    elif not (coeff_a == 0 and coeff_b == 0 and coeff_c == 0):
        print(' = 0')


if __name__ == "__main__":
    main()
