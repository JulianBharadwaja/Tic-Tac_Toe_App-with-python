#------Global Variables------

#Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#If game is still going
game_still_going = True

#Who won? or tie?
winner = None

#who turns is it?
current_player = 'X'
#Displaying Game Board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#Play game of tie tac toe
def play_game():
  #display initial board
  display_board()

  while game_still_going:
    #Handle a single turn of an arbitrary player
    handle_turn(current_player)
    #Check if the game over!
    check_if_game_over()
    # Flip to the other player
    flip_player()
  #The game has ended!
  if winner == 'X' or winner == 'O':
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

#Handle a single player of an arbitrary player!
def handle_turn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1 to 9: ")
  #check the input is correct
  valid = False 
  while not valid:
    while position not in ['1','2','3','4','5','6','7','8','9']:
      position = input("Invalid input! Choose a position from 1 to 9: ")
    #indexing the position
    position = int(position) - 1
    #checking if its position is the same or not
    if board[position] == '-':
      valid = True
    else:
      print("You can go again!")
  


  board[position] = player

  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  #setting global variable for all functions
  global winner
  #check rows
  row_winner = check_rows()
  #check cols
  column_winner = check_columns()
  #check diagonals
  diagonals_winner = check_diagonals()
  if row_winner:
    #there was a win
    winner = row_winner
  elif column_winner:
    #there was a win 
    winner = column_winner
  elif diagonals_winner:
    #there was a win
    winner = diagonals_winner
  else:
    #there was no win
    winner = None
  return

#Checking the rows of the board
def check_rows():
  #set up global variables
  global game_still_going
  #check if any of the rows have all the same value and its not empty
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'
  #if
  if row_1 or row_2 or row_3:
    game_still_going = False
  #return the winner 
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  #set up global variables
  global game_still_going
  #check if any of the rows have all the same value and its not empty
  column_1 = board[0] == board[3] == board[6] != '-'
  column_2 = board[1] == board[4] == board[7] != '-'
  column_3 = board[2] == board[5] == board[8] != '-'
  #if
  if column_1 or column_2 or column_3:
    game_still_going = False
  #return the winner x or o
  if column_1:
    return board[0]
  elif column_2: 
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  #set up global variables
  global game_still_going
  #check if any of the rows have all the same value and its not empty
  diagonals_1 = board[0] == board[4] == board[8] != '-'
  diagonals_2 = board[2] == board[4] == board[6] != '-'
  #if
  if diagonals_1 or diagonals_2:
    game_still_going = False
  #return the winner x or o
  if diagonals_1:
    return board[0]
  elif diagonals_2: 
    return board[2]
  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False

  return

def flip_player():
  #set up global variables we need 
  global current_player
  # if the current player is x then change it to 0 ... vice versa
  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X'
  return

play_game()
# board
# display board
# play game function
# handle turn
# check win function
  #check rows
  #check columns
  #check diagonals
# check tie function 
# flip player 