# python 学习
# 练习
# 开发时间： 2020/10/10 12:24
# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('HelloWord')
print("HelloWord")

# 含有运算符的表达式
print(3+1)

# 将数据输出文件中  注意点 1 所指定的盘符要存在 2. 使用file=fp
fp = open('D:/text.txt', 'a+')   # a+如果文件不存在就创建，存在就在文件内容的后面继续追加
print('HelloWord', file=fp)
fp.close()

# 进行不换行输出 （输出内容在一行当中）
print('hello', 'world', 'Python')
