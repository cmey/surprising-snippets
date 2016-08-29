# Can't round() a Numpy array - have to use np.round().
import numpy as np  # 1.11.1
round(1)
round(np.array(1))  # <-- TypeError: type numpy.ndarray doesn't define __round__ method

# To be fair, Python can't round a list, to begin with.
round([1])  # <-- TypeError: type list doesn't define __round__ method
