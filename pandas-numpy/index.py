import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# arr = np.zeros([3,4])
# print(arr)

# arr = np.ones([3, 4])*5
# print(arr)

# arr = np.arange(10,100,10)
# print(arr)

# arr = np.arange(12).reshape(3,4)    
# print(arr)

#ndim   --> boyut sayısını verir
#shape  --> dizi boyutunu verir
#size   --> dizideki eleman sayısını verir
#dtype  --> dizinin eleman türünü verir,

# arr2Boyutlu = np.arange(12).reshape(3,4)
# arr3Boyutlu = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# # print(arr2Boyutlu.ndim)
# # print(arr3Boyutlu.ndim)
# # print(arr2Boyutlu.shape)
# # print(arr3Boyutlu.shape)
# # print(arr2Boyutlu.size)
# # print(arr3Boyutlu.size)
# print(arr2Boyutlu.dtype)
# print(arr3Boyutlu.dtype)


# arr = np.array([1,2,3,4,5])
arr = np.array([1,2,3,4,5],np.uint16)
print(arr.dtype)
