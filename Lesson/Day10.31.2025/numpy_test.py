import numpy as np
A = np.array([[4,2,6],[7,9,10]])
print("Shape of A:", A.shape)
print(A)
Af = np.array([1,2,3], float)
print("Shape of Af:", Af.shape)
print(Af)
Bf = np.arange(1,10,2)
print("Shape of Bf:", Bf.shape)
print(Bf)

print("Create an array of zeros with shape (3,3):")
arr = np.zeros((3, 3), dtype=int)
print(arr)

print("Create an array of ones with shape (2,4):")
print(np.linspace(0, 2*np.pi, 4))

# Tạo mảng 1D (1 chiều)
rand1D = np.random.rand(5)      
# Tạo mảng 2D (2 chiều)
rand2D = np.random.rand(3,5)     

print(rand1D)
print(rand2D)

print("Random number examples:")
# In ra 5 số nguyên ngẫu nhiên trong khoảng [1, 10)
print(np.random.randint(1, 10, 5)) 

# In ra 5 số ngẫu nhiên theo phân phối chuẩn (mean=0, std=1)
print(np.random.randn(5))             

# In ra 4 số ngẫu nhiên trong khoảng [2, 5)
print(np.random.uniform(2, 5, 4))

# Tạo một mảng
arr = np.array([1, 2, 3, 4, 5])

# Xáo trộn mảng 'arr' (thay đổi trực tiếp mảng gốc)
np.random.shuffle(arr)

print(arr)

