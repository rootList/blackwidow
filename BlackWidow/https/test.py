'''
Created on 2018年4月4日

@author: chentao
'''

def fib(maxNum,num=0):
    print(num)
    a, b = 0,1
    while b<maxNum:
        print(a)
        a,b = b,a+b

def createGenerator() :
    mylist = range(30)
    for i in mylist :
        yield i*i

def lam(n):
    return lambda x:x+n
def list2(lists):
    return [x*2 for x in lists]
    
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
i=2
def fun(num=i, max_num=20, str="is ok"):
    print(num,max_num,str)
    
mygenerator = createGenerator() # create a generator

i=3
args = [3, 50, "no"]
args.extend([123,34])
l = [50]
print(args.index(l, 0,10))
print(args)
#print(list(range(*args)))
#fun(args)