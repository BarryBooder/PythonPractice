password = int(input("请输入你的密码："))
key = 7
print("原密码：", password)
password = password << key
print("加密后:", password)
password = password >> key
print("解密后：", password)