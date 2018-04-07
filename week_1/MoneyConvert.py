#MoneyConvert.py
#人民币表示为RMB***，美元表示为USD***
money = input()
if money[2] in ['D']:
    C = eval(money[3:])*6.78
    print("RMB{:.2f}".format(C))
elif money[2] in ['B']:
    F = eval(money[3:]) / 6.78
    print("USD{:.2f}".format(F))
else:
    print("输入的格式错误")