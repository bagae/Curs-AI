import numpy as np
arr = np.array([1, 2, 3, np.nan, 5])
mean_val = np.nanmean(arr)
arr[np.isnan(arr)] = mean_val
print(arr)
print(np.arange(0,10,2))
print(np.linspace(0,10,5))
print(np.eye(3))
print(arr.shape)
print(arr.ndim)
arr2=np.zeros(2)
print(arr2)