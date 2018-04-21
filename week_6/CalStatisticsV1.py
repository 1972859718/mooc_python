# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 17:33:37 2018

@author: moon
"""

#CalStatisticsV1.py
def getNum():   #获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入一个数字（按回车停止输入）:")
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr = input("请输入一个数字（按回车停止输入）:")
    return nums

def mean(numbers):  #计算平均值
    s =  0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def dev(numbers, mean):     #计算方差
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean)**2
    return pow(sdev / (len(numbers)-1),0.5)

def median(numbers):    #计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNum()
m = mean(n)
print("平均值:{}，方差:{:.2}，中位数:{}.".format(m, dev(n,m), median(n)))