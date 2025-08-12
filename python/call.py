# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         d=a+b
#         print("sum of init is ",d)

#     def __call__(self,a,b):
#         c= a+b
#         print("sum of call is ",c)

# a=A(2,3)
# a(3,5)

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        d=a+b
        print("sum of init is ",d)

    def __call__(self,a,b):
        c= a+b
        print("sum of call is ",c)

a=A(2,3)
a(3,5)