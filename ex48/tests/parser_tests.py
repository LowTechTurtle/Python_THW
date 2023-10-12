from ex48.parser import *
from nose.tools import *

def test_peek():
    words_list = [('noun', 'turtle'), ('verb', 'ran')]
    assert_equal(peek(words_list), 'noun')
    words_list2 = []
    assert_equal(peek(words_list2), None)

def test_match():
    words_list = [('noun', 'turtle'), ('verb', 'ran')]
    assert_equal(match(words_list, 'noun'), ('noun', 'turtle'))
    assert_not_equal(match(words_list, 'verb'), ('noun', 'turtle'))
    assert_equal(match(words_list, 'banana'), None)

def test_skip():
     words_list = [('noun', 'turtle'), ('noun', 'fish'), ('noun', 'bear')]
     skip(words_list, 'noun')
     assert_equal(match(words_list, 'noun'), None)

def test_parse():
    list1 = [('noun', 'turtle'), ('stop', 'is'), ('verb', 'eating'), ('stop', 'a'), ('noun', 'banana')]
    assert_equal(parse_sub(list1), ('noun', 'turtle'))
    assert_raises(ParserError, parse_obj, list1)
    assert_equal(parse_verb(list1), ('verb', 'eating'))
    assert_raises(ParserError, parse_verb, list1)
    assert_equal(parse_obj(list1), ('noun', 'banana'))
    assert_raises(ParserError, parse_sub, list1)
    assert_raises(ParserError, parse_obj, list1)
    assert_raises(ParserError, parse_verb, list1)

