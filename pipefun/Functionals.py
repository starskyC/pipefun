_id = lambda x:x
curry = lambda argc: lambda fn, args = tuple(): fn(*args) if argc == 0 else lambda x: curry(argc - 1)(fn, (*args, x))
apply = lambda *args: lambda fn: fn(*args)

add = lambda a, b: a + b
square = lambda x: x ** 2
sqrt = lambda x: x ** .5

reduce = lambda fn: lambda xs, y = None: [(y := fn(x, y)) for x in xs][-1]
mapFunc = lambda fn: lambda xs: [fn(x) for x in xs]
filterFunc = lambda fn: lambda xs: [x for x in xs if fn(x)]

compose = lambda *fs: (lambda _f=_id: [_f := ( lambda h,g: lambda *args: h(g(*args)) )(f, _f) for f in fs][-1])()
rcompose = lambda *fs: (lambda _f=_id: [_f := ( lambda h,g: lambda *args: g(h(*args)) )(f, _f) for f in fs][-1])()
