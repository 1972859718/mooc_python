#递归函数进行反转
def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs("abcd"))
#字符串切片操作进行反转
print("abcd"[::-1])
