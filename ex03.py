#计算:熟悉python的计算语法，直接用数字进行比较时输出的是布尔型结果
#float 类型可以使用Decimal进行十进制的计算
from decimal import Decimal
print("I will count my chickens")

print("Hens:", 25 + 30 / 6)
print("roosters:", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 -7?")
print(3 + 2< 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("that's why it's False")
print("How about some more")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

x = 4.12
y = 3.96
x = Decimal(str(x))
y = Decimal(str(y))
print(x+y)