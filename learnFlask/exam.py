m = [2, 0, -3, 8, -4, -9]
n = 6
k=1
for i in range(0,n-1):
    print(k)
    if((m[i] == 0) and (m[i+1] == 0)):
        k=1
    elif(m[i+1] == 0):
        k=m[i]
    elif(m[i] == 0):
        k=1
    else:
        k=k*m[i]
        if(k*m[i+1]<0):
            k=1        
print(k)