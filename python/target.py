# target is ---> 9
# return index
# lst=[3,5,7,8,4,2,6,84,1,6,5,2]

lst=[3,5,7,8,4,2,6,8,1,6,5,2]
target=9
lenght = len(lst)
print(lenght)
sort={}
for i in range(0,lenght):
    for j in range(i+1,lenght):
        if lst[j]<lst[i]:
            lst[i],lst[j]=lst[j],lst[i]
newlst=list(set(lst))
print(newlst)    
for i in range(0,lenght):
    for j in range(i+1,lenght):
        print(lst[i]+lst[-1])