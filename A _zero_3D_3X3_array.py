import numpy as np

print("A 3D array with 3 elements in each dimension, initialized with zeros")
array_3d = np.zeros([3, 3, 3])
print(array_3d)

print()
print("Printing out the shape of the array")

# create a 2x2 array
arr_2x2 = np.array([[1, 2], [3, 4]])

# create a 3x3 array
arr_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# check the shape of the arrays
shape_2x2 = arr_2x2.shape
shape_3x3 = arr_3x3.shape

# print the shapes
print(shape_2x2)  # output: (2, 2)
print(shape_3x3)  # output: (3, 3)
