# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
	   
    
    d={'A1': (0, 0),'A2': (0, 1),'A3': (0, 2),'A4': (0, 3),'A5': (0, 4),'B1': (1, 0),'B2': (1, 1),
       'B3': (1, 2),'B4': (1, 3),'B5': (1, 4),'C1': (2, 0),'C2': (2, 1),'C3': (2, 2),
       'C4': (2, 3),'C5': (2, 4),'D1': (3, 0),'D2': (3, 1),'D3': (3, 2),'D4': (3, 3),
       'D5': (3, 4),'E1': (4, 0),'E2': (4, 1),'E3': (4, 2),'E4': (4, 3),'E5': (4, 4)}
    
    if str(s) in d:
        return d[str(s)]
    else:
        raise ValueError
    
  

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
	
	#input will be a tuple i.e. 1,4 or ('1', '4')
    #s =  location

    #if (int(s[0]) > 0 and int(s[0]) <= 4) and (int(s[1]) > 0 and int(s[1]) <= 4):
     #   return str(s[0])+str(s[1])
    #else:
     #   raise ValueError('Input data is out of range')
        
    d = {(0, 0): 'A1', (0, 1): 'A2', (0, 2): 'A3', (0, 3): 'A4', (0, 4): 'A5',
         (1, 0): 'B1',(1, 1): 'B2',(1, 2): 'B3',(1, 3): 'B4', (1, 4): 'B5',
         (2, 0): 'C1',(2, 1): 'C2',(2, 2): 'C3',(2, 3): 'C4',(2, 4): 'C5',
         (3, 0): 'D1',(3, 1): 'D2',(3, 2): 'D3',(3, 3): 'D4',(3, 4): 'D5',
         (4, 0): 'E1',(4, 1): 'E2',(4, 2): 'E3',(4, 3): 'E4',(4, 4): 'E5'}
    if (location) in d:
        return d[(location)]
    else:
        raise ValueError
  

def at(location):
	"""Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
	
    #board = get_board()
    
	return board[int(location[0])][int(location[1])]
    
	
	

def all_locations():
    """Returns a list of all 25 locations on the board."""
	
    all_location = []
	
    for i in range(len(board)):
        for j in range(len(board[i])):
            all_location.append(((i),(j)))

    return all_location
    
	
def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    
    
    # let direction be given as up, down, left, right
    # location
    # location input will be a tuple i.e. 1,4 or ('1', '4')

    (row, column) = location

    location = location
    direction = str(direction)

    if direction == "up":
        return location[0] - 1, location[1]

    elif direction == "down":
        return location[0] + 1, location[1]

    elif direction == "right":
        return location[0], location[1]+1
    else:
        return location[0], location[1] - 1




def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    
    
    if at(location) != "M":
      raise ValueError('There is no musketeer at this location')
    else:
      return at(location) == "M" and is_within_board(location, direction) and at(adjacent_location(location, direction)) == "R"
    

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location) != "R":
     raise ValueError('There is no enemy at this location')
    else:
      return at(location) == "R" and is_within_board(location, direction) and at(adjacent_location(location, direction)) == "-"

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    
    if at(location) == "M":
      return is_legal_move_by_musketeer(location, direction)
    elif at(location) == "R":
      return is_legal_move_by_enemy(location, direction)
    
      

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    
    # find the piece at the location - M or R
    # check if there is a legal move in all four directions and if they are valid
    #if there is at least a legal move in any direction return true, 
    #else return false
    
    a = is_legal_move(location, "left")
    b = is_legal_move(location, "right")
    c = is_legal_move(location, "up")
    d = is_legal_move(location, "down") 
    if a == True or b == True or c == True or d == True:
      return True
    else:
      return False
  
    
  

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    return all_possible_moves_for(who) != [] 
    


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    
    list = []
    
    if is_legal_move(location, "left") == True:
      list.append("left")
    if is_legal_move(location, "up") == True:
      list.append("up")
    if is_legal_move(location, "right") == True:
      list.append("right")
    if is_legal_move(location, "down") == True:
      list.append("down")
    
    return list


def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    
    #return (int(location[0]) > 0 and int(location[0]) <= 4) and (int(location[1]) > 0 and int(location[1]) <= 4)
    return (int(location[0]) >= 0 and int(location[0]) <= 4) and (int(location[1]) >= 0 and int(location[1]) <= 4)
      
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    
    return is_legal_location(adjacent_location(location, direction))        
    
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    
    alloutput=[]
    
    for location in all_locations():
      if at(location) == player:
        for direction in possible_moves_from(location):
          alloutput.append((location, direction))
    return alloutput

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    new = adjacent_location(location, direction)
    
    board [new[0]][new[1]] = at(location)
    board[location[0]][location[1]] = "-"
    

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    
    #initial approach will be a random choice from the list of available moves
    
    import random
    
    return random.choice(all_possible_moves_for(who))
    
  

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    # the idea of the code below is to look for three in a row...
    #it scans from left to right...checks to see if there are 3 M across or down
    #will need to check is the new locatons are valid/legal and within the board...
    #it might come up with index errors...lets see...
    a = "MMM" in ("").join(board[0])
    b = "MMM" in ("").join(board[1])
    c = "MMM" in ("").join(board[2])
    d = "MMM" in ("").join(board[3])
    e = "MMM" in ("").join(board[4])


    #for columns...
    f = "MMM" in ("").join([board[0][0], board[1][0], board[2][0], board[3][0], board[4][0]])
    g = "MMM" in ("").join([board[0][1], board[1][1], board[2][1], board[3][1], board[4][1]])
    h = "MMM" in ("").join([board[0][2], board[1][2], board[2][2], board[3][2], board[4][2]])
    i = "MMM" in ("").join([board[0][3], board[1][3], board[2][3], board[3][3], board[4][3]])
    j = "MMM" in ("").join([board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]])



    return any([a,b,c,d,e,f,g,h,i,j])
    



#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
