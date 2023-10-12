from inputimeout import inputimeout, TimeoutOccurred
import random
from time import sleep
def attack(time_out):
    try:
        prompt_attack = inputimeout(prompt = 'Attack!\n> ', timeout = time_out)
    except TimeoutOccurred:
        return 'atk_succ'
    else:
        return 'atk_failed'

def evade(time_out):
    try:
        prompt_evade = inputimeout(prompt = 'Evade!\n> ', timeout = time_out)
    except:
        return 'evade_failed'
    else:
        return 'evade_succ'

def fight(player_hp, mob_hp, player_dmg, mob_dmg, mob_name):
    combat_choice = ['attack', 'evade']
#    combat_choice = ['attack'] ##uncomment this for testing purpose
    while True:
        if player_hp <= 0:
            return 'death'; break
        if mob_hp <= 0:
            print(f'You have defeated {mob_name}')
            return 'mob_died'; break
        choice = random.choice(combat_choice)
        if choice == 'attack':
            atk_result = attack(0.3+random.random())  
#            atk_result = attack(0.1)  ##uncomment this for testing purpose
            if atk_result == 'atk_succ':
                print('Attack successfully!')
                mob_hp -= player_dmg
            elif atk_result =='atk_failed':
                print('You missed your opportunity to attack')
        if choice == 'evade':
            evade_result = evade(0.3+random.random())
            if evade_result == 'evade_succ':
                print('Evade successfully')
            elif evade_result == 'evade_failed':
                print('You got hit')
                player_hp -= mob_dmg

def fight_prep(mob_name):
    input(f'Prepare to fight {mob_name}!\n>')
    for i in range (0,3):
        print(f'Fight start in {i+1}'); sleep(1)

def atk_parry():
    try:
        prompt_attack1 = inputimeout(prompt = 'Attack!\n>', timeout = 0.2)
    except TimeoutOccurred:
        pass
    else:
        print('You missed the parry and got hit')
        return 'parry_failed'

    try:
        prompt_attack2 = inputimeout(timeout = 0.15)
    except TimeoutOccurred:
        pass
    else:
        print('You parried him')
        input('Rispote>')
        return 'parry_succ'

    try:
        prompt_attack3= inputimeout(timeout = random.random())
    except TimeoutOccurred:
        return 'atk_succ'
    else:
        print('You missed the parry and got hit')
        return 'parry_failed'

def fight_parry(player_hp, mob_hp, player_dmg, mob_dmg, mob_name):
    combat_choice = ['attack', 'evade']
    while True:
        if player_hp <= 0:
            return 'death'; break
        if mob_hp <=0:
            print(f'You have defeated {mob_name}')
            return 'mob_died'; break
        choice = random.choice(combat_choice)
        if choice == 'attack':
            atk_result = atk_parry()
            if atk_result == 'parry_failed':
                player_hp -= mob_dmg
            elif atk_result == 'parry_succ':
                mob_hp -= player_dmg * 3
            elif atk_result == 'atk_succ':
                print('Attack successfully')
                mob_hp -= player_dmg
        if choice == 'evade':
            evade_result = evade(0.3+random.random())
            if evade_result == 'evade_succ':
                print('Evade successfully')
            elif evade_result == 'evade_failed':
                print('You got hit')
                player_hp -= mob_dmg

            













