from sys import exit
import string
from time import sleep
print('''To play this small game, you will need to type in a number when asked to, otherwise just type in whatever you see fit
-------------------------------------------------------------------------------------------------------------------''')
def gold_room():
    print('Congratulation, you have enter a gold room')
    print('This room has a lot of gold, more than u can imagine... So, how much will u take?')
    print('Type in the number of gold coins you wanna get')
    greed = input('>')
    if greed.isdigit() and int(greed) >= 100: 
        print('You motherfucker is too greedy')
        exit(0)
    elif greed.isdigit() and int(greed) < 100:
        print('Ur good, ur not greedy')
        exit(0)
    else:
        print('Motherfuck, learn to write a number')
        exit(0)

def bear_room():
    print(''' We have a super massive bear in here 
    That bear have a jar of honeyyyy
    And the bear is lying in front of another door
    What will you do to move his bear_ass''')
    print('''    1. Take honey
    2. Taunt bear
    3. Go back to the previous room
    ***Type in 1 or 2 or 3 to decide***''')

    bear_moved = False
    go_str = 'go'
    door_str = 'door'
    taunt_str = 'taunt' 
    while True:
        choice = input('>')
        if choice == '1':
            print('The bear slap in yo face and you died')
            exit(0)
        elif choice == '2' and not bear_moved:
            print('His bear_ass has moved, you wanna go through the door or taunt him some more?')
            bear_moved = True
        elif ((go_str in choice.lower()) or (door_str in choice.lower())) and bear_moved:
            gold_room() 
        elif taunt_str in choice.lower():
            print('The bear is infuriated and slap you super super hard')
            print("You Died")
            exit(0)
        elif choice == '3':
            start()
        else: 
            print('You mistyped right? I\'ma give you another chance by restarting the game')
            bear_room()
def start():
    print('You awake in a pretty dark room, the light is too dim')
    print('However, you can perceive that there are two door, one on the left, the other on the right')
    print('Where would you go?')
    choice = input('>')
    if "left" in choice.lower():
        bear_room()
    if "right" in choice.lower():
        wolf_room()
    else:
        print('You cant decide what door u wanted to go, you feel dizzy and suddenly collapsed')
        sleep(2)
        start()
def wolf_room():
    print('You find a pack of wolves in here')
    print('Act wisely, or you will be their first nutrious meal today, fatty')
    sleep(3)
    print('You realize that there is a greatsword on your left and a greatshield on your right')
    print('Of course that you cant wield them both')
    print('What will you do?')
    sleep(4)
    print('1. Take the greatsword')
    print('2. Take the greashield')
    print('3. Fuck these guy, im just going back')
    print("***choose a number from 1 to 3***")
    choice = input('>')
    if choice == '1':
        print('You wanna charge in or let them come at you?')
        choice1 = input('>')
        if ('charge' in choice1.lower()):
            print('You fought bravely, you killed them all but you fainted')
            print('Shouldnt have chose this hell room')
            start()
        if (('let' in choice1.lower()) or ('come' in choice1.lower())):
            print('Luckily, you kill all of them and survived')
            print('Now you choose the next door on the left or in the front?')
            while True:
                choice2 = input('>')
                if ('left' in choice2.lower()):
                    bear_room()
                elif('front' in choice2.lower()):
                    gold_room()
                else:
                    print('I didnt quite understand that, type in again')
    if choice == '2':
        print('Oh greatshield, my old companion, you should charge for the next door and ignore these wolves')
        print('Now you choose the next door on the left or in the front?')
        while True:
            choice3 = input('>')
            if ('left' in choice3.lower()):
                 bear_room()
            elif('front' in choice3.lower()):
                gold_room()
            else:
                print('I didnt quite understand that, type in again')
    if choice == '3':
        print('That was a good decision, but while you going back, a wolf bited your ass and you may or may not fucked')
        start()
    else:
        print('You stumble around not choosing anything and these wolves eat you alive')
        print("You Died")
        exit(0)

# let the fun begin
start()


    

