import numpy as np
# 1. Khoi tao array 2D, co 5 dong, 5 cot, gia tri phan tu la int, tu 10->30

arr = np.random.randint(10, 31, size=(5,5))
print(arr)

# 2. reshape thanh array 1D

arr_1d = arr.reshape(-1)
print("Reshaped to 1D:")
print(arr_1d)
# 3. Extract items in array which is odd numbers

arr_odd = arr[arr%2==1]
print("Odd numbers:")
print(arr_odd)

# 5. Get common items between numpy arrays? (arr1, arr2)
print("Common items between odd numbers and original array:")
print(np.intersect1d(arr_1d, arr_odd))

# 4. replace odd numbers in arr with -1

arr[arr%2 == 1] = -1
print("Array after replacing odd numbers with -1:")
print(arr)

# 6. Find the max value in 1D array
print("Max value in 1D array:")
print(np.max(arr_1d))