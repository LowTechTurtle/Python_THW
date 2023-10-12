from turtle_tool import *
from textwrap import dedent
from sys import exit
from time import sleep
class LowerUndeadBridge():
    def start(self, hp, dmg):
        print('Welcome to the Lower Undead Bridge, this is the one and only path to the earth core')
        print('You see a  hollowed undead in your path')
        print('Just the sight of it make your skin crawl, most people cant believe such an abomination really exists')
        print('You know well this one is strong, but you need to fight it anyway')
        fight_prep('the hollowed undead')
        hp_base = hp
        fight1 = fight_parry(hp, 5, dmg, 2, 'foul undead')
        if fight1 == 'death':
            return 'the_great_fire', 'death', '', '', ''
        elif fight1 == 'mob_died':
            print(dedent('''
            After killing that walking corpse, you proceed through the bridge to the "under-world"
            After that you go deep down,suddenly you feel overwhelming demon-like aura
            You know that something's off, so you drawed your sword and prepared for imminent death
            A big, tall and hairy orc showed up coming to you
           '''))
        print('BOSS FIGHT: Ferocious of the Orc')
        fight_prep('Chief Orc')
        fight2 = fight_parry(hp, 30, dmg, 2, 'Chief Orc')
        if fight2 == 'death':
            return 'the_great_fire', 'death', '', '', ''
        if fight2 == 'mob_died':
            print(dedent('''
            It was a very tough fight, only chosen undead could pulled that off
            You felt dizzy and exhausted after this, and you almost fell down the ground
            But passing out in a place like this also mean death
            Luckily, after walking for a while, you found a lodge
            '''))
            print('You leveled_up,You will invest your new power_point into strength or vitality?')
            while True:
                choice = input('>')
                if ('strength' in choice):
                    return 'lower_lodge', '', 'str_up', '', 'lvl_up'; break
                elif ('vitality' in choice):
                    return 'lower_lodge', '', '', 'vit_up', 'lvl_up'; break
                else:
                    print('I didnt quite understand that, please type in "strength" or "vitality"')

            



        




