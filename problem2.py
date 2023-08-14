def fibonacci(index):
    if(index==1):
        return 1
    if(index==2):
        return 2
    else:
        return(fibonacci(index-1) + fibonacci(index-2))

sum = 0
index = 1
term = fibonacci(1)
while(term<=4000000):
    if(term%2==0):
        sum+=term
    index+=1
    term = fibonacci(index)

print(" Sum of even-vaued terms not greater than 4M = " , sum)