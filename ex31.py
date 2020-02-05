print("""u enter a dark room with two doors.
do u go through door #1 or door #2""")
door = input(">")
if door == "1":
    print('there is a bear eating cake,what do u do')
    bear = input("1.take the cake\n2.scream at the bear")
    if bear == "1":
        print('bear eat u')
    elif bear == "2":
        print('bear eat u too hh')
    else:
        print(f'well doing{bear} is better')
elif door == "2":
    print("u stare into the endless abyss at cthulhu's retina")
    print("1.blueberries")
    print('2.yellow jacket clothespins')
    print('3.understanding resolvers yelling melodies')
    insanity = input('>')

    if insanity == "1" or "2":
        print('your body survives powered by a mind of jello')
    else:
        print('the insanity rots your eyes into a pool of muck')
else:
    print('byebye')