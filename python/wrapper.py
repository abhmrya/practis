# def decora(fun):
#         def wrapper(*args,**Kwargs):
#             print('before the func run')
#             fun(*args,**Kwargs)
#             print('after the fun run')
#         return wrapper
# @decora
# def SayHello(args):
#     print(f"{args}")

# print(SayHello("hii"))

#****************************

# def decora(fun):
#         def wrapper(*args,**Kwargs):
#             print('before the func run')
#             result = fun(*args,**Kwargs)
#             print('after the fun run')
#             return result
#         return wrapper
# @decora
# def SayHello(args):
#     print(f"{args}")
#     return f'complete the task---{args}'

# print(SayHello("hii"))

#*************************************

def decora(fun):
    count=0
    def __init__(self):
         decora.count+=1

    def wrapper(*args,**Kwargs):
        print('before the func run')
        result = fun(*args,**Kwargs)
        print('after the fun run')
        return result
    return wrapper

    @classmethod
    def test(cls):
            print(f'this is show count{cls.count}')

@decora
def SayHello(args):
    print(f"{args}")
    return f'complete the task---{args}'
print(SayHello("hii"))
SayHello.test()