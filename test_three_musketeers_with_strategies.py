import pytest
from three_musketeers import *


left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]


board2 =  [ [_, _, _, M, _],
            [_, _, M, R, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]


board3 = [ [R, R, _, M, _],
            [R, R, R, _, _],
            [R, R, R, _, M],
            [R, R, R, _, _],
            [M, R, R, R, R] ]

#musketeer move should be B5 to C5



def test_create_board():
    create_board()
    assert at((2,2)) == M
    assert at((0,4)) == M

def test_create_board():
  create_board()
  assert at((2,0)) == R
  assert at((4,0)) == M
  assert at((2,2)) == M
	#eventually add at least two more test cases
	#test all other locations of the musketeers

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_set_board():
    set_board(board2)
    assert at((0,0)) == _
    assert at((1,2)) == M
    assert at((1,3)) == R  
	

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_get_board():
    set_board(board2)
    assert board2 == get_board()

def test_string_to_location():
  with pytest.raises(ValueError):
    string_to_location('X3')
    #assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs
  assert string_to_location("A1") == (0,0)
  
def test_string_to_location():
  assert string_to_location("A5") == (0,4)
  with pytest.raises(ValueError):
    string_to_location('A6')
  


def test_location_to_string():
  create_board()
  assert location_to_string((1,3)) == "B4"
  assert location_to_string((2,4)) == "C5"
    
def test_location_to_string():
  with pytest.raises(ValueError):
    location_to_string((2,6))
	

def test_at():
  set_board(board1)
  assert at((3,2)) == "-"


def test_all_locations():
	assert len(all_locations()) == 25
    

def test_adjacent_location():
	assert (adjacent_location((0, 3), "up")) == (-1, 3)
   
    
def test_is_legal_move_by_musketeer():
  set_board(board1)
  assert is_legal_move_by_musketeer((0, 3), "up") == False
    #assert is_legal_move_by_musketeer((2, 2), "down") == True
    
    
def test_is_legal_move_by_enemy():
  set_board(board1)
  assert is_legal_move_by_enemy((1, 2), "up") == True
  assert is_legal_move_by_enemy((4, 3), "right") == True
  with pytest.raises(ValueError):
    is_legal_move_by_enemy((1, 1), "right")
    
   

def test_is_legal_move():
  set_board(board1)
  assert is_legal_move((4, 3), "right") == True
    

def test_can_move_piece_at():
  set_board(board1)
  assert can_move_piece_at((2,2)) == True

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((1,1)) == False


def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # # Eventually put at least three additional tests here
    # # with at least one additional board
    
def test_has_some_legal_move_somewhere():
    set_board(board2)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True

def test_possible_moves_from():
	#assert possible_moves_from((2,2)) == ["left", "up", "right"]
    set_board(board1)
    #assert possible_moves_from((1,3)) == ["left", "down"]
    #assert possible_moves_from((0,3)) == []
    assert possible_moves_from((4,3)) == ['left', 'up', 'right']
    

def test_is_legal_location():
	assert is_legal_location((1,5)) == False
   

def test_is_within_board():
	assert is_within_board((4, 3), "down") == False
    #assert is_within_board((3, 3), "down") == True
    

def test_all_possible_moves_for():
	assert all_possible_moves_for('M') == [((1,3),"left"), ((1,3),"down"), ((2,2),"left"), ((2,2),"up"), ((2,2),"right") ]
    
    
def test_make_move():
	#assert make_move((2, 3), "right") == True
    pass
    
def test_choose_computer_move():
	#assert choose_computer_move('M') == True
    # # Replace with tests; should work for both 'M' and 'R'
    
    # a bit difficult to test as the algorithm can return different choices each time...
    set_board(board3)
    assert choose_computer_move(M) == ((4,0), "up") or ((4,0), "right")
    

def test_is_enemy_win():
    set_board(board2)  
	
    assert is_enemy_win() == False
    # # Replace with tests


