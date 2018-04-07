plaincode=input()
for p in plaincode:
    if ord("a")<=ord(p)<=ord("z"):#ord()将ASSCLL码转为字符
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end='')
        ###+3是加密 -3是解密 C=(P+3)mod26  加密
        ###p=(c-3)mod26 解密
    elif ord("A")<=ord(p)<=ord("Z"):#大写
        print(chr(ord("A")+(ord(p)-ord("A")+3)%26),end='')
    else:
         print(p,end = '')