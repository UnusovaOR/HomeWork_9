from main import get_count
def test_get_count_good_data():
    lines = ['1,0,3,4,5,6,1,8,9,10,11,12,C"',
             '1,0,3,4,5,6,5,8,9,10,11,12,Q"',
             '1,0,3,4,5,6,10,8,9,10,11,12,S"',
             '1,0,3,4,5,6,15,8,9,10,11,12,C"',
             '1,1,3,4,5,6,15,8,9,10,11,12,Q"']
    assert get_count(lines, 18) == (2, 1, 1)
def test_get_count_bad_age():
    lines = ['1,0,3,4,5,6,999,8,9,10,11,12,C"',
             '1,0,3,4,5,6,888,8,9,10,11,12,Q"',
             '1,0,3,4,5,6,10,8,9,10,11,12,S"',
             '1,0,3,4,5,6,15,8,9,10,11,12,C"',
             '1,1,3,4,5,6,15,8,9,10,11,12,Q"']
    assert get_count(lines, 18) == (1, 0, 1)
def test_get_count_bad_embarked():
    lines = ['1,0,3,4,5,6,1,8,9,10,11,12,Шербур"',
             '1,0,3,4,5,6,5,8,9,10,11,12,Q"',
             '1,0,3,4,5,6,10,8,9,10,11,12,Саутгемптон"',
             '1,0,3,4,5,6,15,8,9,10,11,12,C"',
             '1,1,3,4,5,6,15,8,9,10,11,12,Q"']
    assert get_count(lines, 18) == (1, 1, 0)
