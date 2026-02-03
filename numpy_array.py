import numpy as np

# Read dimensions
n, m = map(int, input().split())

# Read the array
arr = np.array([list(map(int, input().split())) for _ in range(n)])

# Sum along axis 0
sum_axis_0 = np.sum(arr, axis=0)

# Product of the result
result = np.prod(sum_axis_0)

print(result)
