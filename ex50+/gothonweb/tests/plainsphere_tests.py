from nose.tools import *
from gothonweb.planisphere import *

def test_room():
    gold = room('Gold Room', 'This room has a lot of gold')
    assert_equal(gold.name, 'Gold Room')
    assert_equal(gold.paths, {})

def test_room_path():
    center = room('center', 'test room in the center')
    north = room('north', 'test room in the north')
    south = room('south', 'test room in the south')
    center.add_paths({'north': north})
    center.add_paths({'south': south})
    north.add_paths({'south': center})
    south.add_paths({'north': center})
    assert_equal(center.go('north'), north)
    assert_equal(north.go('south'), center)
    assert_equal(south.go('south'), None)

def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)
    assert_equal(start_room.go('tell a joke'), laser_weapon_armory)
