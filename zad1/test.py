from Function import *
from bisection import *
from falsi import *

if __name__ == '__main__':
    fn = Function("x^3+x^2-x")
    x0bi, ibi = bisection(fn, -10, -0.5, epsilon=0.1)
    x0falsi, ifalsi = falsi(fn, -10, -0.5, epsilon=0.1)
    print("""------------------------------------------------
x^3+x^2-x, a=-10, b=-0.5, epsilon=0.1""")
    print("bisection:", x0bi, ibi)
    print("falsi:", x0falsi, ifalsi)
