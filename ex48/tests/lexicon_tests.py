from ex48.lexicon import *
from nose.tools import *

def test_direction():
    assert_equal(scan("north"), [('direction', 'north')])
    result = scan('north south east')
    assert_equal(result, [('direction', 'north'), ('direction', 'south'), ('direction', 'east')])

def test_number():
    assert_equal(scan('123'), [('number', 123)])
    assert_equal(scan('123123 9883'), [('number', 123123), ('number', 9883)])

def test_error():
    assert_equal(scan('ASDFGHJKL'), [('error', 'ASDFGHJKL')])
    assert_equal(scan('bear IAS princess'), [('noun', 'bear'),
                                               ('error', 'IAS'),
                                               ('noun', 'princess')])

class Tests_asdf():
    def test_error(self):
        assert_equal(scan('ASDFGHJKL'), [('error', 'ASDFGHJKL')])
    def test_number(self):
        assert_equal(scan('123'), [('number', 123)])

