import copy

# Shallow copy
a=[1,2,3,[4,5,6]]

s=copy.copy(a)
s[3][0]=7
# print(a)
# print(s)

# deep copy
c=[1,2,3,[4,5,6],7]
d=copy.deepcopy(c)
d[3][0]=7
# print(c)
# print(d)

e=copy.deepcopy(c)
e[0]=8
# print(c)
# print(e)

f=[1,2,3,4,5,6,7]
g=copy.deepcopy(f)
g[3]=5
# print(f)
# print(g)

h=[1,2,3,[4,5,[6,7,8,9]]]
i=copy.deepcopy(h)
i[3][2][0]=10
# print(h)
# print(i)