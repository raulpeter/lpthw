from sys import exit

def reward():
    print('u save the girl,come and get your reward')
    choice = input("how much money do u like?")
    how_much = int(choice)
    if how_much < 10000:
        print("u worth it")
        exit(0)
    else:
        over("u are too greedy")
def evil():
    print("how would like to fight evil?\n ")
    evil_happy = False
    while True:
        choice = input('>')
        if choice == "give him a shot":
            over('emm, u are too stupid')
        elif choice == 'tell him a joke' and not evil_happy:
            print('u save the girl,go and get her')
            evil_happy = True
        elif choice == 'tell him a joke' and evil_happy:
            over('your joke is not funny enough')
        elif choice == 'get the girl' and evil_happy:
            reward()
        else:
            print('I got no idea what that means')
def maze():
    print('here u are in a maze')
    print('do u want go inside? or go away')
    choice = input('>')
    if "go away" in choice:
        start()
    elif"go inside" in choice:
        over('that was tasty')
    else:
        maze()
def over(why):
    print(why)
    exit(0)
def start():
    print('u are going to save your girlfriend')
    print('u go left or right')
    choice = input('>')
    if choice =='left':
        evil()
    elif choice =='right':
        maze()
    else:
        over('u lost your girl')
start()