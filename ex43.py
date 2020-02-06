from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene!=last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()
class Death(Scene):
    quips = ['you died','hello']
    def enter(self):
        print(Death.quips[randint(0,len(self.quips-1))])
        exit(1)
class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""the #25 have invaded your ship"""))
        action = input('>')
        if action =='shoot':
            print(dedent("""u shoot,u die"""))
            return 'death'
        elif action =='dodge':
            print(dedent("""gothon eats u"""))
            return 'death'
        elif action == 'tell a joke':
            print(dedent("""jump through the weapon armory door"""))
            return 'laser_weapon_armory'
        else:
            print('does not compute')
            return 'central_corridor'
class LaserWeaponArmory(Scene):
    def enter(self):
        print('the code is 3 digits')
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input('')
        guesses = 0
        while guess!=code and guesses<10:
            print('bzzzzzeddd')
            guesses+=1
            guess = input("")
        if guess == code:
            print('u can go to bridge')
            return 'the bridge'
        else:
            print('game over')
            return 'death'
class TheBridge(Scene):
    def enter(self):
        action = input()
        if action == 'throw the bomb':
            print('u die')
            return 'death'
        elif action == 'slowly place the bomb':
            print('escape pod')
            return 'escape_pod'
        else:
            print('does not compute')
            return 'the_bridge'
class EscapePod(Scene):
    def enter(self):
        print('which one u like')
        good_pod = randint(1,5)
        guess = input()
        if int(guess)!= good_pod:
            print('u die')
            return 'death'
        else:
            print('u won')
            return 'finished'
class Finished(Scene):
    def enter(self):
        print('u won')
        return 'finished'
class Map(object):
    scenes = {'central_corridor':CentralCorridor(),'laser_weapon_armory':LaserWeaponArmory(),'the_bridge':TheBridge(),'escape_pod':EscapePod(),'death':Death(),'finished':Finished()}
    def __init__(self,start_scene):
        self.start_scene = start_scene
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()