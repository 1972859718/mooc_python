import random
#以10为随机数种子生成5个随机数
random.seed(10)
for i in range(5):
    print(random.random())
print("分隔符".center(50,'#'))
#生成5个[1，10]之间的随机整数
for i in range(5):
    print(random.randint(1,10))
print("分隔符".center(50,'#'))
#生成5个[1,20)之间的以2为步长的随机数
for i in range (5):
    print(random.randrange(1,20,2))
print("分隔符".center(50,'#'))
#生成两个8比特长的随机整数
print(random.getrandbits(8))
print(random.getrandbits(8))
print("分隔符".center(50,'#'))
#生成5个[1,10]之间的随机小数
for i in range(5):
    print(random.uniform(1,10))
print("分隔符".center(50,'#'))
#从序列中选择一个元素
s = [1,2,3,4,5,6,7,8,9]
print(random.choice(s))
print("分隔符".center(50,'#'))
#将序列中的元素随机排列，返回打乱后的序列
random.shuffle(s)
print(s)
