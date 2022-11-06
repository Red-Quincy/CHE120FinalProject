 # Tic-Tac-Toe
import random  #random is a package, the random value package, we have decleare this if we want to import the random package (RW) 

def drawBoard(board):
       # This function prints out the board that it was passed.
       # "board" is a list of 10 strings representing the board (ignore index 0).
      print(board[7] + '|' + board[8] + '|' + board[9]) #Each board[*] represents a spot on the tictactoe board. Currently, they are just empty spaces but will eventually correspond to a move made by the player/computer (QW)
      print('-+-+-')
      print(board[4] + '|' + board[5] + '|' + board[6])
      print('-+-+-')
      print(board[1] + '|' + board[2] + '|' + board[3])
def inputPlayerLetter():
      # Lets the player type which letter they want to be.
      # Returns a list with the player's letter as the first item and the computer's letter as the second.
      letter = ''
      while not (letter == 'X' or letter == 'O'):
          print('Do you want to be X or O?')
          letter = input().upper() # Formats the user input to be uppercase so that the program can properly compare values (QW)

      # The first element in the list is the player's letter; the second is the computer's letter.
      if letter == 'X':
          return ['X', 'O']
      else:
         return ['O', 'X']
def whoGoesFirst():
      # Randomly choose which player goes first.
      if random.randint(0, 1) == 0:
          return 'computer'                              #Return the turn to computere. Computer plays first. (RW)
      else:
          return 'player'                                #Else returns the turn to the player. Player plays first. (RW)

def makeMove(board, letter, move): 
      board[move] = letter #Recall: board is the section of the tictactoe board. Here, that section is being assigned to the move (QW)

def isWinner(bo, le):
      # Given a board and a player's letter, this function returns True if that player has won.
      # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
      (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
      (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
      (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
      (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
      (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
      (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
      (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal
      #This is accounting for all possible win scenarios for the player (QW)
def getBoardCopy(board):
      # Make a copy of the board list and return it.
      boardCopy = []
      for i in board:
          boardCopy.append(i)
      return boardCopy

def isSpaceFree(board, move):
      # Return True if the passed move is free on the passed board.
      return board[move] == ' '

def getPlayerMove(board):
      # Let the player enter their move.
      move = ' '
      while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)): #The while loop will only break once 1-9 has been selected, and only if the space is freee (QW)
          print('What is your next move? (1-9)')
          move = input() #The integer assigned to move is where the player is making their move (QW)
      return int(move)

def chooseRandomMoveFromList(board, movesList):
      # Returns a valid move from the passed list on the passed board.
      # Returns None if there is no valid move.
      possibleMoves = []
      for i in movesList:
          if isSpaceFree(board, i):
              possibleMoves.append(i)

      if len(possibleMoves) != 0:
          return random.choice(possibleMoves)
      else:
          return None

def getComputerMove(board, computerLetter):
      # Given a board and the computer's letter, determine where to move and return that move.
 if computerLetter == 'X':
          playerLetter = 'O'
 else:
          playerLetter = 'X'

      # Here is the algorithm for our Tic-Tac-Toe AI:
      # First, check if we can win in the next move.
 for i in range(1, 10):
          boardCopy = getBoardCopy(board)
          if isSpaceFree(boardCopy, i):
              makeMove(boardCopy, computerLetter, i)
              if isWinner(boardCopy, computerLetter):
                  return i

      # Check if the player could win on their next move and block them.
 for i in range(1, 10):
         boardCopy = getBoardCopy(board)
         if isSpaceFree(boardCopy, i):
             makeMove(boardCopy, playerLetter, i)
             if isWinner(boardCopy, playerLetter):
                 return i

     # Try to take one of the corners, if they are free.
 move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
 if move != None:
         return move

     # Try to take the center, if it is free.
 if isSpaceFree(board, 5):
  return 5

     # Move on one of the sides.
  return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
     # Return True if every space on the board has been taken. Otherwise, return False.
     for i in range(1, 10):
         if isSpaceFree(board, i):
             return False
     return True


print('Welcome to Tic-Tac-Toe!') #This is the "start" of the program. Everything up to this point has been defining functions that will be used throughout the course of the game (QW)

while True:
 # Reset the board.
 theBoard = [' '] * 10 #theBoard is a list of 10 empty spots (they're not actually empty, they still have the quotations but the quotations surround an empty spot) (QW)
 playerLetter, computerLetter = inputPlayerLetter() #Since inputPlayerLetter will return two values, the program assigns the users letter as the first value and the computers letter as the second (QW)
 turn = whoGoesFirst() #Calls the function used to randomly assign the start player. Line 130 informs the user who the assigned start player was.(QW)
 print('The ' + turn + ' will go first.')
 gameIsPlaying = True

 while gameIsPlaying:
  if turn == 'player':
   # Player's turn
   drawBoard(theBoard) #Draw out the board, with empty slots for each section (QW)
   move = getPlayerMove(theBoard) #Get the move from the player (QW)
   makeMove(theBoard, playerLetter, move) #Draw the board according to the move (QW)

   if isWinner(theBoard, playerLetter): #check if the player won the game (QW)
    drawBoard(theBoard)
    print('Hooray! You have won the game!')
    gameIsPlaying = False
   else:
    if isBoardFull(theBoard): #Check if the board is full, and thus a tie (QW)
     drawBoard(theBoard)
     print('The game is a tie!')
     break
    else:
     turn = 'computer' #If you haven't won nor is the game a tie, pass the turn to the computer (QW)

  else:
   # Computer's turn
   move = getComputerMove(theBoard, computerLetter)
   makeMove(theBoard, computerLetter, move)

   if isWinner(theBoard, computerLetter):
    drawBoard(theBoard)
    print('The computer has beaten you! You lose.')
    gameIsPlaying = False
   else:
    if isBoardFull(theBoard):
     drawBoard(theBoard)
     print('The game is a tie!')
     break
    else:
     turn = 'player'
 print('Do you want to play again? (yes or no)') 
 if not input().lower().startswith('y'): #If no, run line 170. If yes, restart the loop and resume the game(QW)
  break #Breaks the while gameIsPlaying loop, this ending the game (QW)
