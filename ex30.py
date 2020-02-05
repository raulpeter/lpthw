#if-else
people = 30
cars = 40
trucks = 15

if cars > people:
    print('we should take cars')
elif cars < people:
    print('we should not take cars')
else:
    print('we cannot decide')

if trucks > cars:
    print('too many trucks')
elif trucks < cars:
    print('we could take trucks')
else:
    print('we still cannnot decide')

if people > trucks:
    print("let's take trucks")
else:
    print("let's stay at home")