# my methos but time complsity is max

ls1=[23,-13,25,65,-645,45,-26,85,-53,-76,75,36,55]
maxx=0
for i in ls1:
    for j in ls1:
        k=i*j
        if maxx<k:
            maxx=k
        else:
            pass
print(maxx)

# chhatgpt
# 1st sort them fiest 2 and last 2 multipy and return max
ls2=sorted(ls1)
print(ls2)
multiply_first_2=ls2[0]*ls2[1]
multiply_last_2=ls2[-1]*ls2[-2]
if multiply_first_2>multiply_last_2:
    print("first two digit & didgit is ",multiply_first_2,ls2[0],ls2[1])
else:
    print("last two digit & didgit is ",multiply_last_2,ls2[-1],ls2[-2])


    
#<********************diffrence between time complasity******************>
import time
import random
def twomaxnumber(*num):
    maxx=0
    start=time.time()
    for i in num:
        for j in num:
            k=i*j
            if maxx<k:
                maxx=k
            else:
                pass
            start2=time.time()
            # print(start2)
    print('time1',start2-start)
    return maxx
numbers = [random.randint(1, 1000) for _ in range(10000)]
print('number1',twomaxnumber(*numbers))

def twomaxnumbersort(*args):
    time1=time.time()
    ls2=sorted(*args)
    multiply_first_2=ls2[0]*ls2[1]
    multiply_last_2=ls2[-1]*ls2[-2]
    if multiply_first_2>multiply_last_2:
        print("first two digit & didgit is ",multiply_first_2,ls2[0],ls2[1])
    else:
        print("last two digit & didgit is ",multiply_last_2,ls2[-1],ls2[-2])
    time2=time.time()
    print('time2',time2-time1)
num=[random.randint(1,1000) for _ in range(10000)]
print('number2',twomaxnumbersort(num))