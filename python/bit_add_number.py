def add(a,b):
    while b!=0:
        carry=a&b
        a=a^b
        b=carry<<1
        # print(a)
        # print(b)
    return a
# print(add(5,7))

# def sub(a,b):
#     return add(a,add(~b,1))

print(add(7,5)) 
# print(sub(7,5))    
