import numpy as np
x=5
v=np.array([1,2,3,4,5]) #vettore monodimensionale
m=np.array([[1,2,3,4,5],[6,7,8,9,10]]) # array bidimensionale
t=np.array([
    [
        [1,2],[3,4]
        ],
    [
        [5,6],[7,8],
        ]
    ]) # tensore
print(t.shape)

a=np.array([1,2,3,4,5])
b=10
print (a+b)