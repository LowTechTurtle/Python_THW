from sys import exit, argv
import random
from textwrap import dedent
class Scene:
    def enter(self):
        pass

class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        self.current_scene = self.scene_map.scenes.get('central_corridor')
        last_scene = self.scene_map.scenes.get('escape_pod')
        while self.current_scene != last_scene:
#        while True:
            next_scene = self.current_scene.enter(self)
            self.current_scene = self.scene_map.scenes.get(next_scene)
        self.current_scene.enter(self)
class Death(Scene):
    def enter(self):
        print('You Died')
        exit(0)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent('''You have entered the central corridor, seeing there is a Gorthon
        What will you do?
        1. Take the sword on the floor and fight
        2. Try to fuck him up bare handed
        3. Tell him a joke'''))
        choice = input('>')
        if choice == '1' :
            print('You fought badly, died worst')
            return 'death'
        elif choice == '2' :
            print('You had no chance at all, he\'s a warrior and fully armed')
            print('Who are you to fight him bare handed?')
            print('You fought bravely, but that\'s all what there is')
            return 'death'
        elif choice == '3' :
            print('Your joke is so stupid that he bursted into laughing')
            print('You got the sword and fucked him with it while he\'s laughing')
            return 'laser_weapon_armory'
        else:
            print('Learn how to write, motherfucker')
            return 'central_corridor'

class LaserweaponArmory(Scene):
    def enter(self):
        print(dedent('''You have entered the laser weapon armory, you need to get the neutral bomb
        But it requires the code, its 3 digit code
        You have 10 guesses, if you get it all wrong then ur doomed'''))
        code = ''.join([str(random.randint(0, 9)) for i in range(0, 3)])
        guesses = 0
        print(f'cheat_code is {code}')
        
        while True:
            if guesses < 10:
                print('Guesses number ', guesses +1)
                guess = input('>')
                if guess == code:
                    print('You got the code right')
                    return 'the_bridge'
                else:
                    print('You got it wrong')
                    guesses += 1
            else:
                print('Ur done')
                return 'death'


class TheBridge(Scene):
    def enter(self):
        print(dedent('''So far so good, we got a gun on the way we got here, we thought we set these fuckers on fire and escape
        However, you find 5 Gothons on the bridge
        What will you do?
        1. Shoot these Gothons
        2. Slowly place the bomb and point the gun to the bomb'''))
        choice = input('>')
        if choice == '1':
            print('That was 5 against 1, how stupid are you?')
            print('Well, you dropped the bomb and get shot')
            return 'death'
        elif choice == '2':
            print('The Gothons know what is it means if they shoot you')
            print('So they backed off, you set time for the bomb and still point the gun to the bomb')
            print('You get into the escape pod room and blast the door, they cant chase you now')
            return 'escape_pod'
        else:
            print('Learn how to write, motherfucker')
            return 'the_bridge'



class EscapePod(Scene):
    def enter(self):
        print('Congrats, you have reached the escape pod')
        print('Say goodbye to these losers')
        input('>')
        exit(0)
class Map:
    scenes = {'escape_pod': EscapePod,
              'the_bridge': TheBridge,
              'laser_weapon_armory':LaserweaponArmory,
              'death': Death,
              'central_corridor': CentralCorridor
              }

    def __init__(self, start_scene):
        print(dedent('''You crew get killed, your ship is being taken over
        The terrifying Gothons is coming
        Do what must be done, after then, you may live'''))
    
    def next_scene(self, scene_name):
        pass 
    
    def opening_scene(self):
        pass

a_map = Map('central_corridor')

a_game = Engine(a_map)

a_game.play()
