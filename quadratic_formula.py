import math


def quadraticFormula(a, b, c):
    ''' Implementing quadratic formula avoiding catastrophic cancellation '''

    try:
        r1 = (2 * c) / (-b - math.sqrt((b**2) - (4*a*c)))
        r2 = (2 * c) / (-b + math.sqrt((b**2) - (4*a*c)))
        print(f"Root 1: {r1} \nRoot 2: {r2}")
    except:
        print(
            f"[ERROR] - Math domain error when computing a = {a}, b = {b}, c = {c}. Try again!")


if __name__ == '__main__':

    print("--------")
    quadraticFormula(4, 4, -30)
    print("--------")
    quadraticFormula(2, 4, -30)
    print("--------")
    quadraticFormula(6, -17, 12)
    print("--------")
    quadraticFormula(1, -3, 3)      # Testing error
    print("--------")
    quadraticFormula(1, -7, -3)
    print("--------")
