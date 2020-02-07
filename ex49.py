from parser import *
from nose.tools import *

def test_get_type():
    list1 = [('verb', 'do')]
    assert_equal(get_type(list1), 'verb')
    list2 = [('verb', 'do'), ('stop', 'the')]
    assert_equal(get_type(list2), 'verb')
    list3 = [(None, None)]
    assert_equal(get_type(list3), None)

def test_match():
    list1 = [('verb', 'do'), ('stop', 'the'),('noun', 'homework')]

    assert_equal(match(list1, 'verb'),('verb', 'do'))
    assert_equal(match(list1, 'stop'),('stop', 'the'))

    list2 = [(None, None)]
    assert_equal(match(list2, 123),None)
    assert_equal(list2, [])
    assert_equal(match(list2, 123),"list Null")

def test_skip():
    list1 = [('verb', 'do'),('stop', 'the'),('noun', 'homework')]
    assert_equal(skip(list1,'verb'),('verb', 'do'))
    assert_equal(skip(list1,'stop'),None)

def test_parse_object():
    list1 = [('verb', 'do'),('stop', 'the'),('noun', 'homework')]
    assert_equal(parse_object(list1), ('noun', 'homework'))
    assert_raises(ParserError, parse_object, list1)

def test_parse_subject():
    list1 = [('verb', 'do'), ('stop', 'the'), ('noun', 'homework')]
    assert_equal(parse_subject(list1), ('noun', 'player'))
    parse_verb(list1)
    assert_equal(parse_subject(list1), ('noun', 'homework'))
    assert_raises(ParserError, parse_subject, list1)

def test_parse_sentence():
    list1 = [('verb', 'do'), ('stop', 'the'), ('noun', 'homework')]
    sentence = parse_sentence(list1)
    assert_equal(sentence.subj,  'player')
    assert_equal(sentence.verb,  'do')
    assert_equal(sentence.obj,  'homework')

