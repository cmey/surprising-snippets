# A variable imbued with pint unit mutates its state when touched by Numpy.
# Source https://github.com/hgrecco/pint/blob/master/pint/quantity.py#L1165-L1167
# Since https://github.com/hgrecco/pint/commit/53d5fca35948a5bb80cb900e8e692e8206b1512a
import pint  # 0.7.2
import numpy as np  # 1.11.1

units = pint.UnitRegistry()
x = 1 * units.s

print(type(x._magnitude), x._magnitude)
np.array(x)  # <-- This affects x. Note ignored return value. Expected dead code.
print(type(x._magnitude), x._magnitude)

# Worse, it breaks round().
print(round(x))
print(round(y))  # TypeError: type numpy.ndarray doesn't define __round__ method
