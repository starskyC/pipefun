# Pipefun

A simple, lightweighted, zero dependency python piping package.

## Install
```bash
pip install pipefun
```

## Usage
```python
from pipefun import Pipable, out
from pipefun.Functionals import square

add_to = lambda a: lambda b: a + b # a curried **add** function

output = ~(x >> add_to(3) >> square)

print(output) # 36
```

The `>>` operator pushes a `Pipable` into a function and return a new `Pipable` with the return value of the function.
The `~` operator pulls the value in a `Pipable`

**Note that `Pipable` is *immutable*, so the returned `Pipable` doesn't equal the input and is a new one**
```python
x_out = x >> add_to(3) >> square

print(x_out == x) # False
print(~x_out == ~x) # False
```

### Pipe merging
In daily use case, it's very possible that functions take more than 1 arg. To handle this, `Pipable` can store more than 1 values and plug them into a function when needed.

We use the `|` operator to merge `Pipable`s. In Python, it has lower priority than `>>`. 

```python
x = Pipable(3)
y = Pipable(5)

out = x >> square # Pipable(9)

# merge two Pipables together
out = out | y # Pipable(9, 5)

# plug the pipes into a two args function
out = out >> add # Pipable(14)

print(~out) # 14
```

Alternatively, in one line.
```python
out = ( x >> square | y) >> add # Pipable(14)
print(~out) # 14
```

### Let's discard the `~` operator
There is a special function in Pipable package that do nothing. If a Pipable is piped into it, same thing will happen with what the `~` operator do.
```python
from pipefun import Pipable, out

x = Pipable(2)

y = x >> square >> out
print(y) # 4
```
