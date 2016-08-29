# Numpy converts a list of tuples *not* into an array of tuples, but into a 2D
# array instead.
import numpy as np  # 1.11.1

list_of_tuples = [(1, 2), (3, 4)]
print('list of tuples:', list_of_tuples, 'type:', type(list_of_tuples))

A = np.array(list_of_tuples)
print('numpy array of tuples:', A, 'type:', type(A))


# It makes computing unique rows trickier than it should:
unique_A, indices_to_A = np.unique(list_of_tuples, return_inverse=True)
print('naive numpy unique:', unique_A, 'and indices:', indices_to_A)  # WRONG!

# Workaround to do np.unique by row (http://stackoverflow.com/a/8024764/3438463)
A_by_row = np.empty(len(list_of_tuples), object)
A_by_row[:] = list_of_tuples
unique_A, indices_to_A = np.unique(A_by_row, return_inverse=True)
print('unique tuples:', unique_A, 'and indices:', indices_to_A)
