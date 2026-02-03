import numpy as np

# Read dimensions
n, m = map(int, input().split())

# Read the array
arr = np.array([list(map(int, input().split())) for _ in range(n)])

# Min along axis 1
row_min = np.min(arr, axis=1)

# Max of the result
result = np.max(row_min)

print(result)
5