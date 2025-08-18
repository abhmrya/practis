lst=['ab','cd','ef','gh']

print(type(lst))
last=lst.pop(-1)
print(last)
print(lst)
print([last]+lst)


lst=['ab','cd','ef','gh']
print(lst)
last=lst.pop(-1)
lst.insert(0, last)
print(lst)


# remove 20 and insert 25
lst = [10, 20, 30, 40, 50]
last = lst.pop(1)
print(last)
lst.insert(1,25)
print(lst)

lst = [10, 20, 30, 40, 50]
element=25
for i in lst:
    if i==30:
        lst.insert()