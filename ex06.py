#更多的格式化输出
types_of_people = 10
x = f"there are {types_of_people} types of people"
binary = "binary"
do_not ="don't"
y = f"those who know{binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I said: '{y}'")

hilatious = False
joke_evaluation = "isn't that joke so funny? {}"
print(joke_evaluation.format(hilatious))#新知识

w = 'this is'
e = 'an apple'
print(w+e)