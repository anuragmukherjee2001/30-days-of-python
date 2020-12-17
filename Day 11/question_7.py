import math

def solve_quadratic_eqn(a, b, c):
    x1 = (-b + math.sqrt((b * b) - (4 * a * c)))/(2 * a)
    x2 = (-b - math.sqrt((b * b) - (4 * a * c)))/(2 * a)
    print("The roots are: ", x1, x2)

solve_quadratic_eqn(4, 16, 2)    