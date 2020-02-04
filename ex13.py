传参
from sys import argv

script, first, second, third = argv #相当于为函数传参铺垫基础

print("the script is called:", script)
print("your first variable is :", first)
print("your second variable is :", second)
print("your third variable is :", third)

a = input("please input script")
b = input("please input first")
c = input("please input second")
d = input("please input third")

print(a,b,c,d)