from sys import exit
from random import randint

class Room(object):
    def enter(self):
        print("undone")
        exit(1)
class Engine(object):
    def __init__(self,room_map):
        self.room_map = room_map
    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('finished')
        while current_room!=last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)
        current_room.enter()
class Over(Room):
    quips = ['it is over','hello','bye']
    def enter(self):
        print(self.quips[randint(0,len(self.quips)-1)])
        exit(1)
class Room1(Room):
    def enter(self):
        print("""which one would u like to go""")
        action = input('>')
        if action =='1':
            print("""u die""")
            return 'over'
        elif action =='2':
            print("""good game""")
            return 'over'
        elif action == '3':
            print("""ok,u can go to the next room""")
            return 'room2'
        else:
            print('please input again')
            return 'room1'
class Room2(Room):
    def enter(self):
        print('the code is 3 digits')
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input('')
        guesses = 0
        while guess!=code and guesses<10:
            print('u are wrong')
            guesses+=1
            guess = input("")
        if guess == code:
            print('u can go to room3')
            return 'room3'
        else:
            print('game over')
            return 'over'
class Room3(Room):
    def enter(self):
        action = input()
        if action == '1':
            print('u die')
            return 'over'
        elif action == '2':
            print('u can go to room4')
            return 'room4'
        else:
            print('please input again')
            return 'room3'
class Room4(Room):
    def enter(self):
        print('which one u like')
        good_pod = randint(1,5)
        guess = input()
        if int(guess)!= good_pod:
            print('u die')
            return 'over'
        else:
            print('u won')
            return 'finished'
class Finished(Room):
    def enter(self):
        print('u won')
        return 'finished'
class Map(object):
    rooms = {'room1':Room1(),'room2':Room2(),'room3':Room3(),'room4':Room4(),'over':Over(),'finished':Finished()}
    def __init__(self,start_room):
        self.start_room = start_room
    def next_room(self,room_name):
        val = Map.rooms.get(room_name)
        return val
    def opening_room(self):
        return self.next_room(self.start_room)

map = Map('room1')
game = Engine(map)
game.play()