#函数的返回值相关
def add(a,b):
    print(f"adding{a}+{b}")
    return a+b
def subtract(a,b):
    print(f"subtracting{a}-{b}")
    return a-b
def multiply(a,b):
    print(f"mutiplying{a}*{b}")
    return a*b
def divide(a,b):
    print(f"dividing{a}/{b}")
    return a/b
print("let's do some math")

age = add(30,5)
height = subtract(78,4)
weighty = multiply(90,2)
iq = divide(100,2)
print(f"age:{age}, height:{height}, weight:{weighty}, iq:{iq}")

print("here is a puzzle")

what = add(age,subtract(height,multiply(weighty,divide(iq,2))))
print(what)