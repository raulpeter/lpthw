from sys import exit

def gold_room():
    print('the room is full of gold how much do u take')
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man,learn to type a number")
    if how_much < 50:
        print("nice u are not greedy,u win")
        exit(0)
    else:
        dead("u greedy bastard")
def bear_room():
    print("there is a bear here.\nthe bear has a bunch of honey\nhow are u going to move the bear?")
    bear_moved = False
    while True:#无限循环
        choice = input('>')
        if choice == "take honey":
            dead('the bear eat u')
        elif choice == 'taunt bear' and not bear_moved:
            print('u can go through now')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('the bear eat u')
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print('I got no idea what that means')
def cthulhu_room():
    print('here u see the great evil cthulhu')
    print('do u flee for your life or eat your head?')
    choice = input('>')
    if "flee" in choice:
        start()
    elif"head" in choice:
        dead('that was tasty')
    else:
        cthulhu_room()
def dead(why):
    print(why,'good job')
    exit(0)
def start():
    print('u are in a dark room')
    print('u go left or right?')
    choice = input('>')
    if choice =='left':
        bear_room()
    elif choice =='right':
        cthulhu_room()
    else:
        dead('u starve to death')
start()