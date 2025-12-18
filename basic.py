import numpy as np 

data = np.array([1,2,3,4,5])

data1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]])

data2 = np.array([[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],
                  [16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],
                  [31,32,33,34,35],[36,37,38,39,40],[41,42,43,44,45]]])

data3 = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
                  [['J','K','L'], ['M','N','O'], ['P','Q','R']],
                  [['S','T','U'], ['V','W','X'], ['Y','Z','']]])                  

data = data*2

print(data)
print(type(data))

print(data1.ndim)
print(data2.ndim)
print(data2.shape)

print("\nchain Indexing")
print(data2[0][1][2])

dob=data2[0][0][0]*10 +data2[0][1][1]
print(dob)

name = (
    data3[2,1,0] +
    data3[0,1,1] +
    data3[0,1,0] +
    data3[0,0,0] +
    data3[1,1,1] +
    data3[2,0,1]
)


print(name)