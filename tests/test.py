from os import getcwd
import sys
sys.path.append(getcwd())

from pipefun.Pipable import Pipable, out
from pipefun.Functionals import add, square, curry

x = Pipable(3)

add_to = curry(2)(add)

print( x >> add_to(3) >> square >> out ) # 36

x = Pipable(3)
y = Pipable(5)

print( (x >> square | y) >> add >> out ) # 14
