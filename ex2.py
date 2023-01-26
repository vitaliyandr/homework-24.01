import random
try:
    z,p,r=0,0,100
    A=[random.randint(-200,200) for i in range(r)]
    print(*A)
    for i in range(r):
        if A[i]==0: 
            z+=1
        elif A[i]>0: 
            p+=1
    print("max=",max(A),"  mix=",min(A))
    print ("0=",z,"positive=",p,"negative=",r-p-z)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
