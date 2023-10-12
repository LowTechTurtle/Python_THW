from inputimeout import inputimeout, TimeoutOccurred
from random import random
def atk_parry():
    try:
        prompt_attack1 = inputimeout(prompt = 'Attack!\n>', timeout = 0.15)
    except TimeoutOccurred:
        pass
    else:
        return 'parry_failed'

    try:
        prompt_attack2 = inputimeout(timeout = 0.1)
    except TimeoutOccurred:
        pass
    else:
        return 'parry_succ'
    
    try:
        prompt_attack3 = inputimeout(timeout = random())
    except TimeoutOccurred:
        return 'attack_succ'
    else:
        return 'parry_failed'

x = atk_parry()

print(x)




