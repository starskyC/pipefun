import sys
sys.path.append('..')

from pypipe.Pipable import Pipable, out
from pypipe.Functionals import add, square, curry

x = Pipable(3)

add_currying = curry(2)(add)

print( x >> add_currying(3) >> square >> out ) # 36

x = Pipable(3)
y = Pipable(5)

print( (x >> square | y) >> add >> out ) # 14
