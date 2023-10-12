from map_upper import *
from map_lower import *
import random
from re import findall
from textwrap import dedent
import string
from sys import exit

class Engine():
    def __init__(self, map_obj):
        self.map = map_obj
    def play(self):
        self.current_map = self.map.first_map
##the code in the comment below will crash if player die twice in a row
        death_check = ''
        while True:
            if death_check == '':
                next_map_name, death_check, new_str, new_vit, new_lvl = self.current_map.start(combat.hp, combat.dmg)
                self.current_map = self.map.next_map(next_map_name)
                if new_str:
                    combat.strength += 2
                if new_vit:
                    combat.vit += 1
                if new_lvl:
                    combat.lvl += 1
            if death_check == 'death':
                Death().start()
                next_map_name, death_check, new_str, new_vit, new_lvl = self.current_map.start(combat.hp, combat.dmg)
                self.current_map = self.map.next_map(next_map_name)
            
class Death():
    def start(self):
        print('You died')
        print('Returning to the nearest bonfire')
        input('>')

class Intro():
    def start(self, hp, dmg):
        print(dedent('''
        From a murky land, there are an unknowing maigc, powering the undead, some say that mystic power is called Zel
        Zel is the source of all undead, keeping them from death, make them suffer for eternity
        Being an undead, you also seek to fight and to destroy Zel, so that you can be released from this agony
        '''))
        print('Moving to The Great Fire...')
        return 'the_great_fire', '', '', '', ''

class SaveGame():
    def get_stats(self):
        savefile = open('savefile')
        raw_stats = [line.strip() for line in savefile]
        value_list = []
        for item in raw_stats:
            list_val = findall('.*=(.*)', item)
            string_val = list_val[0]
            value_list.append(string_val)
        savefile.close()
        return value_list
    def write_stats(self, pos, strength, vit, lvl): 
        savefile = open('savefile', 'a+')
        savefile.truncate(0)
        savefile.write(f'current_position={pos}\n')
        savefile.write(f'current_str={strength}\n')
        savefile.write(f'current_vit={vit}\n')
        savefile.write(f'current_level ={lvl}')
        savefile.close()

#Bonfire-like feature
class Bonfire():
    def start(self, hp, dmg):
        welcome_list = ['Welcome to the bonfire, where everyone can have a little rest in a journey that have no ending.',
                        'You have come to the bonfire - a nice place to rest without thinking about these foul hollowed undead',
                        'A bonfire - you have come, here you can have a good rest, a fine place in a world of madness',
                        'Agony and pain you have endured, now you can rest, for you have come to the lovely bonfire']
        print(random.choice(welcome_list))
        combat.hp = divmod(combat.vit, 1)
        value =[i for i in a_map.Room if (a_map.Room[i] == a_game.current_map)]
        save.write_stats(value[0], combat.strength, combat.vit, combat.lvl)
 
class CombatSystem():
    def __init__(self, pos, strength, vit, lvl):
        self.pos = pos
        self.strength = int(strength)
        self.vit = int(vit)
        self.lvl = int(lvl)
    def set_stats(self, pos, strength,vit, lvl, sp):
        self.pos = pos
        self.strength = int(strength)
        self.vit = int(vit)
        self.lvl = int(lvl)
    def health_point(self):
        self.hp, self.hp_decimal = divmod(self.vit, 1)
    def damage(self):
        self.dmg, self.dmg_decimal = divmod(self.strength, 3)

class TheGreatFire():
    def start(self, hp, dmg):
        print('Welcome to The Great Fire - The biggest safe place in this chaos of a world')
        print('At a bonfire, you can rest, heal your wound to ready for adventure')
        print('Your game will be automatically saved at a bonfire')
        print(dedent('''
        Now, we shall go on an adventure, we have two ways:
        The first way is going up to the highest peak of the mountain
        The second way is going down to the core of the earth itself
        The second way is more dangerous and we likely cant go there for now
        But we always have a choice, which way do you want to go to?
        '''))
        choice1 = input('>')
        if ('up' in choice1.lower()) or ('mountain' in choice1.lower()):
            return 'upper_undead_bridge', '', '', '', ''
        elif ('down' in choice1.lower()) or ('core' in choice1.lower()):
            return 'lower_undead_bridge', '', '', '', ''
        else:
            print('I don\'t understand what you means')
            print('Restarting...')
            return 'the_great_fire', '', '', '', ''
class LowerLodge(Bonfire):
    def start(self, hp, dmg):
        super().start(hp, dmg)
        print('Press Enter to continute your journey or type in "exit" to exit the game')
        choice = input('>')
        if choice == '':
            pass
        elif ('exit' == choice.lower()):
            exit(0)


class Map():
    Room = {
            'intro': Intro(),
            'death': Death(),
            'the_great_fire': TheGreatFire(),
            'lower_undead_bridge': LowerUndeadBridge(),
            'upper_undead_bridge': UpperUndeadBridge(),
            'lower_lodge': LowerLodge()
            
            }
    def __init__(self, start_map):
        self.first_map = Map.Room.get(start_map)
    def next_map(self, map_name):
         return Map.Room.get(map_name)

from turtle_tool import *

save = SaveGame()
stats = save.get_stats()
combat = CombatSystem(stats[0], stats[1], stats[2], stats[3])
combat.health_point()
combat.damage()
a_map = Map(stats[0])
a_game = Engine(a_map)
a_game.play()

