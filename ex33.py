# #while循环
# # i = 0
# # numbers = []
# #
# # while i < 6:
# #     numbers.append(i)
# #     i = i+1
# #     print(numbers)
# #     print(f"at the bottom i is {i}")
# # for num in numbers:
# #     print(num)
def while_loop(a,b):
    i = 0
    numbers = []
    while i < a:
        numbers.append(i)
        i = i+b
        print(numbers)

while_loop(6,1)
