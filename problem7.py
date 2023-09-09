def prime(n):
    """ checks is n is prime or not, if prime returns True, otherwise it returns False"""
    flag = True
    if(n==1):
        flag = False
    
    for i in range(2,int(n/2)):
        if(n%i==0):
            flag = False
            break
    return(flag)

num = 2
k = 10001
j = -1
while(j<=k):
    if(prime(num)):
        j+=1
        if(j==k):
            break
        else:
            num+=1
    else:
        num+=1
print(" 10001st prime is ", num)         