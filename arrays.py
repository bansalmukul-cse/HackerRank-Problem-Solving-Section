import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr1 =numpy.array(arr[::-1],float)
    return arr1
    
    
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
