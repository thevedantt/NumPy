import numpy as np 

data = np.array([[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]])

#data[start:stop:step]

print(data[1])
print(data[-1])    
print(data[0:2])   
print(data[::2])
print(data[::-1])

#coulmn selection 
print(data[:,2])
print(data[:,-2])

print(data[0:1,0:3])
print(data[0:2,0:2])

print(data[2:,2:]) 