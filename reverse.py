# <----------------My Solutions-------------->
a=123456789
reverse=[]
r=len(str(a))
if len(str(a))>0:
    for i in range(len(str(a))):
        b=a%10
        a=int(a/10)
        reverse.append(b)
c="".join(str(i) for i in reverse)
print(c)

#<--------------other methos by online-------->
a=123456789
reverse=0
while a>0:
    b=a%10
    reverse=reverse*10+b
    a=a//10
# print(reverse)

# <---------------- remove last element---------------------->
a=123456789
# for i in range(len(str(a))):
#     a=a//10
#     print(a)
while a>0:
    a=a//10
    # print(a)

#<-------------reverse word----------------->
# method 1
d=['a','b','c','d','e','f','g','h','i','j','k','l']
e=d[::-1]
print(e)

print(bool(0))
print(bool(None))
print(bool(False))
print(bool(True))
print(bool(1))

f=['i','love','you']
g=f[::-1]
print(g)
h=[]
for i in g:
    print(i)
    for k in i:
        i=k[::-1]
        h.append(i)
print(h)