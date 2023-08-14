import math
  
def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))

def palindrome(num):
    if(num == rev(num)):
        return(True)
    else:
        return(False)

listA = [x for x in range(100,1000)]
listB = [y for y in range(100,1000)]

listC = []

for i in range(0,len(listA)):
    for j in range(0, len(listB)):
        listC.append(listA[i]*listB[j])


listC.sort(reverse = True)

for number in listC:
    if(palindrome(number)==True):
        print(number)
        break;
