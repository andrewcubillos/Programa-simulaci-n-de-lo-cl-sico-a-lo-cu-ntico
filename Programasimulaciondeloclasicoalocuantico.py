from numeroscomplejos import *
def norm(N):
    return ((((N[0])**2)+((N[1])**2))**(1/2))**2



def state(X,Y,n):
                
    result =[[0 for x in range(len(Y[0]))] for y in range(len(Y))]
    for h in range(n-1):
        for i in range(len(X)):
           
           for j in range(len(Y[0])):
               
               for k in range(len(Y)):
            
                   
                   result[i][j] += X[i][k] * Y[k][j]
            
        Y=result
     
    return result 

def stateprobabilistic(X,Y,n):
    result =[[0 for x in range(len(Y[0]))] for y in range(len(Y))]
    p=X
    result2=[[0 for x in range(len(p[0]))] for y in range(len(p))]
    
    for h in range(n-1):
        for i in range(len(X)):
           
           for j in range(len(p[0])):
               
               for k in range(len(p)):
                   result2[i][j] += X[i][k] * p[k][j]
                   
                        

    for i in range(len(result2)):
       
       for j in range(len(Y[0])):
           
           for k in range(len(Y)):
               result[i][j] += result2[i][k] * Y[k][j]
         
    return result



def quantumstate(X,n):
    Y=X
    result = [[0 for j in range(len(Y[0]))] for i in range(len(Y))]
    ssum=(0,0)
    for h in range(n):
        for i in range(len(X)):
            
           for j in range(len(Y[0])):

               for k in range(len(Y)):
                   result[i][j] =suma(ssum,producto(X[i][k],Y[k][j]))
                   
                   ssum=result[i][j]       
               ssum =(0,0)

    for z in result:
        for m in z:
            if m==(0,0):
                result[result.index(z)][z.index(m)]=0
            elif m==(1,0):
                result[result.index(z)][z.index(m)]=1
            else:
                result[result.index(z)][z.index(m)]=norm(m)
    return result       
