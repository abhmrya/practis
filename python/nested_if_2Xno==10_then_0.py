ls1=[1,2,3,4,5,6,7,8,9,10]
out1=[]
for i in ls1:
    if ls1[i]%2==0:
        ls1[i]=0
        out1.append(ls1[i])
    else:
        out1.append(ls1[i])
# print(out1)

ls2=[[1,2,3,7,13,9,6,32,67,9],[4,12,36,7,3,9]]
out2=[]
for i in ls2:
    out3=[]
    for j in i:
        k=2*j
        if k>20:
            out3.append(0)
        else:
            out3.append(k)
    out2.append(out3)
    print(out3)
print(out2)