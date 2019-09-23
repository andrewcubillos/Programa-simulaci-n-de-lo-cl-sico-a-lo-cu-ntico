
def state(X,Y,n)
    X =[[1 for x in range(6)] for y in range(6)]
    Y=([[1],[2],[3],[4],[5],[6]])
    result =[[0 for x in range(len(Y[0]))] for y in range(len(Y))]
    for h in range(n)
        for i in range(len(X)):
           
           for j in range(len(Y[0])):
               
               for k in range(len(Y)):
                   result[i][j] += X[i][k] * Y[k][j]
                   

print (result)


