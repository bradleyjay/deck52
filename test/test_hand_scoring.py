import pytest   

from ui import Play

def test_fullhouse_4s():
    
    # full house
    X_of_a_kind = {'4': [], '3': ['9'], '2': ['A']}
    flush = False
    straight = False
    selection_sorted = [9, 9, 9, 'A', 'A']
    
    assert Play._hand_scoring(None, None, X_of_a_kind, flush, straight, selection_sorted) == 'Full House: 9s and As'

    # 4s
    X_of_a_kind = {'4': ['4']}
    assert Play._hand_scoring(None, None, X_of_a_kind, flush, straight, selection_sorted) == 'Four of a Kind: 4s'

def test_flush_straight():

    # flush
    X_of_a_kind = {'4': [], '3': [], '2': []}
    flush = True
    straight = False
    selection_sorted = [2, 3, 5, 7, 9]

    assert Play._hand_scoring(None, None, X_of_a_kind, flush, straight, selection_sorted) == 'Flush, 9 high'


    # straight
    # flush
    X_of_a_kind = {'4': [], '3': [], '2': []}
    flush = False
    straight = True
    selection_sorted = [2, 3, 4, 5, 6]

    assert Play._hand_scoring(None, None, X_of_a_kind, flush, straight, selection_sorted) == 'Straight, 6 high'


