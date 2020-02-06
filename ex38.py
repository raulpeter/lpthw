#list
ten_things = "apples oranges crows telephone light sugar"
print('there are not 10 things in that list let us fix it')

stuff = ten_things.split(' ')
more_stuff = ['day','night','song','frisbee','corn','banana','girl','boy']
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding:",next_one)
    stuff.append(next_one)
    print(f'there are {len(stuff)} items now')
print(stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))#返回一个string，中间添加着#