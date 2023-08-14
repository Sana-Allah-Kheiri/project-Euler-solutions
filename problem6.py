sum = 0
for i in range(1,101):
    sum+=i

sqOfSums = sum*sum

sum1 = 0
for i in range(1,101):
    sum1+=(i*i)
    
print(" difference = ", sum1-sqOfSums)