# Assigning to a numpy array can type cast (and lose data).
import numpy as np  # 1.11.1

A = np.ones((3, 2), dtype=np.float32)
B = np.zeros((1, 2), dtype=np.complex64) + 1j

A[0] = B  # <-- # Subtle bug: in A, imaginary part is lost.

print(B)
print(A[0])

# Granted, we get a warning:
# numpy-array-dtype.py:7: ComplexWarning: Casting complex values to real discards the imaginary part

# To turn the warning into a raised exception instead:
np.seterr(all='raise')
# http://stackoverflow.com/questions/15933741/how-do-i-catch-a-numpy-warning-like-its-an-exception-not-just-for-testing
A[0] = B  # <-- # Subtle bug: in A, imaginary part is lost.
