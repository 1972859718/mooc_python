#函数调用
def fact1(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
a = fact1(10)
print(a)
print("分隔符".center(50,'#'))


#可选参数传递
def fact2(n, m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m
print(fact2(10),fact2(10,5))
#上为位置传递参数，下为名称传递参数
print(fact2(m=5,n=10))
print("分隔符".center(50,'#'))


#可变参数传递
def fact3(n,*b):
    s = 1
    for i in range(1,n+1):
        s *= i
    for item in b:
        s *= item
    return s
print(fact3(10,3),fact3(10,3,5,8))
print("分隔符".center(50,'#'))


#函数返回多个值
def fact4(n, m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m,n,m
print(fact4(10,5))
a,b,c = fact4(10,5)
print(a,b,c)
print("分隔符".center(50,'#'))


#函数内用全局变量
n ,s = 10, 100
def fact5(n):
    global s
    for i in range(1,n+1):
        s *= i
    return s         #全局变量
print(fact5(n),s)    #全局变量被修改
print("分隔符".center(50,'#'))


#组合数据类型函数外创建
ls = ['F', 'f']
def func(a):
    ls.append(a)   #ls是全局变量
    return
func('c')          #全局变量ls被修改
print(ls)
print("分隔符".center(50,'#'))


#组合数据类型函数内创建
ls = ['F', 'f']
def func(a):
    ls = []
    ls.append(a)   #ls是局部变量
    return         #局部变量被释放
func('c')          #局部变量ls被修改
print(ls)
print("分隔符".center(50,'#'))


#lambdad函数
f = lambda x, y : x + y
print(f(1,99))
g = lambda : "lambda"
print(g())
