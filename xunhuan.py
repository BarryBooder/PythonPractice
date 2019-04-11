a = int(input("准备计算的首相："))
b = int(input("准备计算的末项："))
c = int(input("循环次数："))
i = 1
d = 1
while i <= c:
    d = d+a+b
    i += 1
    print(d)