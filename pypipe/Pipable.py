from Functionals import mapFunc

out = lambda *xs: xs 

class Pipable():
	def __init__(self, *val):
		self.__vals = val
		self.__arg_count = 1
	

	def __repr__(self):
		return 'Pipable(' + ', '.join(mapFunc(repr)(self.__vals)) + ')'

	__str__ = __repr__
	
	# ~x -> tuple
	def __invert__(self):
		return self.__vals

	# x >> fn -> fn(x)
	def __rshift__(self, fn):
		if fn == out:
			if self.__arg_count == 1:
				return self.__vals[0]
			else:
				return self.__vals

		if fn.__code__.co_argcount < self.__arg_count:
			raise Exception(f'piping {self.__arg_count} into {fn.__code__.co_argcount} channel')

		p = Pipable(fn(*self.__vals))
		p.__arg_count = self.__arg_count

		return p
	
	# x | y -> (x, y)
	def __or__(self, other):
		if isinstance(other, Pipable):
			other = other.__vals
		
		return Pipable(*self.__vals, *other)
		
	def __ror__(self, other):
		if isinstance(other, Pipable):
			other = other.__vals
		
		return Pipable(*other, *self.__vals)
