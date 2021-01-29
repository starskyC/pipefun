from Pipable import Pipable, out

x = Pipable(3)

square = lambda x: x**2
add = lambda a, b: a + b

add_currying = lambda a: lambda b: a + b

print( x >> add_currying(3) >> square >> out ) # 36

x = Pipable(3)
y = Pipable(5)

print( (x >> square | y) >> add >> out ) # 14
