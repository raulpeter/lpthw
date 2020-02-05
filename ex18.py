#函数基础
def print_two(*arg):
    arg1, arg2 = arg
    print(arg1, arg2)
def print_two_again(arg1, arg2):
    print_two(arg1,arg2)
def print_one(arg1):
    print(arg1)
def print_none():
    print("there is nothing")

print_two("sun","chenyu")
print_two_again("sun","chenyu")
print_one("first!")
print_none()