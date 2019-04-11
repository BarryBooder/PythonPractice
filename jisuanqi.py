from functools import reduce
num = int(input("输入需要进行多少次运算："))
i = 1
number = []
while i <= num:
    i += 1
    a = int(input("请输入第{}个数".format(i-1)))
    number.append(a)
type = int(input('请选择您要进行的运算：(1、加法器；2、减法器；3、乘法器；4、除法器)'))
if type == 1:
    typee = "加法器"
    sum = sum(number)
elif type == 2:
    typee = "减法器"
    sum = reduce(lambda x, y: x-y, number)
elif type == 3:
    typee = "乘法器"
    sum = reduce(lambda x, y: x*y, number)
elif type == 4:
    typee = "除法器"
    sum = reduce(lambda x, y: x/y, number)
print("您选择的运算法则为：", typee)
print("您的运算结果为：", sum)