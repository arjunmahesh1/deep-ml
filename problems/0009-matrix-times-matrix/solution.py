def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	#for i in range(len(a)):          
    #for j in range(len(b[0])):
    #    for k in range(len(b)):  
    #        result[i][j] += a[i][k] * b[k][j]
    import numpy as np
    A = np.array(a)
    B = np.array(b)

    if A.shape[1] != B.shape[0]:
        return -1

    return A @ B