from flask import Flask, session, redirect, request, url_for, render_template
from markupsafe import escape
from gothonweb import planisphere
from random import choice
app = Flask(__name__)
room_list = {'central_corridor': 'Central Corridor', 
          'laser_weapon_armory': 'Laser Weapon Armory',
          'the_bridge': 'The Bridge',
          'escape_pod': 'Escape Pod',
          'the_end_winner': 'The End',
          'the_end_loser' : 'The End'}


def hs(current_hc, mapname):
    map_list = ['Central Corridor', 'Laser Weapon Armory', 'The Bridge', 'Escape Pod', 'The End']
    if mapname in map_list:
        for i in range(0, 5):
            if mapname == map_list[i]:
                mapname_count = i
            if current_hc == map_list[i]:
                current_hc_count = i
        if mapname_count >= current_hc_count:
            return mapname
        else:
            return current_hc
    else:
        return current_hc

def hs_num(plan):
    map_list = ['Central Corridor', 'Laser Weapon Armory', 'The Bridge', 'Escape Pod', 'The End']
    for i in range(0, len(map_list)):
        if plan == map_list[i]:
            score = str(i+1)
            return score



user_list = []
password_list = []
highscore_list = []
user_dict = {}
@app.route('/', methods = ['POST', 'GET'])
def index():
    global user_list, password_list, highscore_list, user_dict 
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pass')        
        session[user] = user
        if user in user_list:
            for i in range(0, len(user_list)-1):
                if user_list[i] == user:
                    user_list.pop(i)
                    password_list.pop(i)
                    highscore_list.pop(i)
                    user_dict.pop(user)
        user_list.append(user)
        user_pass = user + password
        session[user_pass] = password
        password_list.append(password)
        user_highscore = user + '_highscore'
        try:
            if session[user_highscore] == None:
                session[user_highscore] = 'Central Corridor'        
        except:
            session[user_highscore] = 'Central Corridor'
        print('this ran #1')
        x = session[user_highscore]
        highscore_list.append(x)
        highscore_realdeal = hs_num(x)
        user_dict.update({user: highscore_realdeal})
        return redirect(url_for(f'prepare', banana = session[user]))
    else:
        return render_template('login_and_choose_map.html')
@app.route('/highscore')
def highscore():
    global user_list, highscore_list, user_dict
    return render_template('highscore_board.html', user_dict = user_dict)

@app.route('/prepare/<banana>', methods = ['POST', 'GET'])
def prepare(banana):
    global user_list, password_list
    session['room_name'] = planisphere.START
    u_len = len(user_list) - 1
    user = user_list[u_len]
#    return redirect(url_for(f'game', banana = session[user]))
    return redirect(url_for(f'game'))

@app.route('/game', methods = ['POST', 'GET'])
def game():
    global user_list, password_list, highscore_list, user_dict
    u_len = len(user_list) - 1
    user = user_list[u_len]
    room_name = session.get('room_name')
    user_highscore = user + '_highscore'
    try:
        name_for_room = room_list[room_name]
        highscore = hs(session[user_highscore], name_for_room)
        session[user_highscore] = highscore
        highscore_list.pop(u_len)
        highscore_list.append(highscore)
        user_dict.pop(user)
        highscore_real = hs_num(highscore)
        user_dict.update({user: highscore_real})
        print(highscore)
        print(user_dict)
    except:
        pass

    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template('show_room.html', room = room)
        else:
            return render_template('you_died.html')
    else:
        room = planisphere.load_room(room_name)
        print(room)
        action = request.form.get('action')
        next_room = room.go(action)
        if next_room == None:
            action = '*'
            next_room = room.go(action)
            if next_room:
                session['room_name'] = planisphere.name_room(next_room)
            else:
                session['room_name'] = planisphere.name_room(room)
        else:
            session['room_name'] = planisphere.name_room(next_room)
        return redirect(url_for(f'game'))


app.secret_key = '4acdfc1cbfa476d6d19f8e2e62b7805c092aa3b9f39c704eb84d336ff644c9e7'

if __name__ == '__main__':
    app.run()
