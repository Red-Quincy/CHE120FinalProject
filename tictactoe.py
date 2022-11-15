 # Tic-Tac-Toe
import random  #random is a package, the random value package - for random numbers, we have decleare this if we want to import the random package (RW) 

def drawBoard(board):
 
       # This function prints out the board that it was passed.
  
       # "board" is a list of 10 strings representing the board (ignore index 0).
   
       #Each board[*] represents a spot on the tictactoe board. Currently, they are just empty spaces but will eventually correspond to a move made by the player/computer (QW)
    
       #The board numbers correspond to the number pad on the keyboard. Hence why square 7, 8 ,9 are at top and square 1, 2, 3 are at the bottom. (RW) 
       #Note, notation for squares is nxm, n = row, m = column.  (RW)
     
      print(board[7] + '|' + board[8] + '|' + board[9]) #Prints the top row in the console - of 3 squares in the 3x3 board. (RW)
      
      print('-+-+-')  #Prints a divider separating the 1st row (1x3) and 2nd row (1x3) in the console display. (RW) 
      
      print(board[4] + '|' + board[5] + '|' + board[6]) #Prints the middle row in the console - of 3 squares in the 3x3 board. (RW)
      
      print('-+-+-')  #Prints a divider separating the 2nd row (1x3) and the 3rd row (1x3) in the console display. (RW)
      
      print(board[1] + '|' + board[2] + '|' + board[3]) #Prints the bottom row in the console - of 3 squares in the 3x3 board. (RW)
      
def inputPlayerLetter():
 
      # Function prompts the player type which letter they want to be. X or 0. (RW)
  
      # Returns a list with the player's letter as the first item and the computer's letter as the second. So player can always choose desired letter against AI. (RW)
   
      letter = ''  #Sets up the variable 'letter' of type str. (RW)
    
      while not (letter == 'X' or letter == 'O'):  
      
      #Evalulates whether variable letter is 'X' or '0', since it's empty the line above, this prompts the user to input their desired letter.   (RW)
      
          print('Do you want to be X or O?')        #Prints question in console. (RW)   
       
          letter = input().upper() # Formats the user input to be uppercase so that the program can properly compare values (QW)

      # The first element in the list is the player's letter; the second is the computer's letter.
      
      if letter == 'X':           #If player chose 'X', then the computer gets '0'. (RW)
          return ['X', 'O']   
      else:
         return ['O', 'X']        #If player chose '0', then the computer gets 'x'. (RW)
       
def whoGoesFirst():
 
      # Randomly decides whether player of AI goes first. This is also why we import random (RW)
      if random.randint(0, 1) == 0:
          return 'computer'                              #Return the turn to computer. Computer plays first. (RW)
      else:
          return 'player'                                #Else returns the turn to the player. Player plays first. (RW)

def makeMove(board, letter, move): 
 
      board[move] = letter #Recall: board is the section of the tictactoe board. Here, that section is being assigned to the move (QW)

def isWinner(bo, le):
 
      # Given a board and a player's letter, this function returns True if that player has won.
      # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
   
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # 3 across the top - 1st row (1x3)        (RW)
      (bo[4] == le and bo[5] == le and bo[6] == le) or # 3 across the middle - 2nd row (1x3)             (RW)
      (bo[1] == le and bo[2] == le and bo[3] == le) or # 3 across the bottom - 3rd row (1x3)             (RW)
      (bo[7] == le and bo[4] == le and bo[1] == le) or # 3 down the left side - 1st column (3x1)         (RW)
      (bo[8] == le and bo[5] == le and bo[2] == le) or # 3 down the middle - 2nd column (3x1)            (RW)
      (bo[9] == le and bo[6] == le and bo[3] == le) or # 3 down the right side - 3rd column (3x1)        (RW)
      (bo[7] == le and bo[5] == le and bo[3] == le) or # 3 diagonal, top left to bot right.              (RW)
      (bo[9] == le and bo[5] == le and bo[1] == le)) # 3 Diagonal, bot left to top right.                (RW)
   
      #This is accounting for all possible win scenarios for the player (QW)
    
    #RAY ^^^^^^^^^^
    
def getBoardCopy(board):
      # Make a copy of the board list and return it.
      boardCopy = []
      for i in board: # Loops "i" for within the board, adding "i" to the list. (JH)
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
      for i in movesList: # Loops "i" within the movelist (JH)
          if isSpaceFree(board, i): # If the board space is free in "i", then go to next line (JH)
              possibleMoves.append(i) #add I to list possibleMoves (JH)

      if len(possibleMoves) != 0: # If the list has something in it, go to next line (JH)
          return random.choice(possibleMoves) #return a random value within the list possibleMoves (JH)
      else:
          return None

def getComputerMove(board, computerLetter): # THIS SPECIFIC FUNCTION IS XIUWEN
      # Given a board and the computer's letter, determine where to move and return that move.
 if computerLetter == 'X': 
          playerLetter = 'O' # If computerLetter is going to be "X", then correspond playerLetter to "O"
 else:
          playerLetter = 'X' # If computerLetter is not "X", then playerLetter will be "X"

      # Here is the algorithm for our Tic-Tac-Toe AI:
      # First, check if we can win in the next move.
 for i in range(1, 10): # Loop "i" as the numbers 1 to 9 (range(1,10)) into this system. (XD)
          boardCopy = getBoardCopy(board) # Create boardCopy from previous getBoardCopy function to implement into this loop. (XD)
          if isSpaceFree(boardCopy, i): # If the boardCopy space is free coressponding to "i", then move to next line. (XD)
              makeMove(boardCopy, computerLetter, i) # Make the coressponding space for given "i" equal to computerLetter. EX: If i = 3 and ComputerLetter = "X", then boardCopy(3) = "X". (XD)
              if isWinner(boardCopy, computerLetter): # Checks if the boardCopy[1-9] is equal to computerLetter, if yes, returns "i". (XD)
                  return i

      # Check if the player could win on their next move and block them.
 for i in range(1, 10): # Loops i from 1 to 9. (XD)
         boardCopy = getBoardCopy(board)  # Copies boardCopy from getBoardCopy function. (XD)
         if isSpaceFree(boardCopy, i): # If the boardCopy space is free coressponding to "i", then move to next line. (XD)
             makeMove(boardCopy, playerLetter, i) # Make the coressponding space for given "i" equal to playerLetter. EX: If i = 6 and playerLetter = "O", then boardCopy(6) = "O". (XD)
             if isWinner(boardCopy, playerLetter): # Checks if the boardCopy[1,...,9] is equal to playerLetter, if yes return "i". (XD)
                 return i

     # Try to take one of the corners, if they are free
 move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) # Makes computer choose from [1,3,7,9] randomly (XD)
 if move != None: # If no no corners are available, return move. (XD)
         return move

     # Try to take the center, if it is free.
 if isSpaceFree(board, 5): # Lets computer choose center if all corners are unavailable. (XD)
  return 5

     # Move on one of the sides.
  return chooseRandomMoveFromList(board, [2, 4, 6, 8]) # Returns board[2,4,6,8] in a random order if middle and corners are all taken. (XD)

def isBoardFull(board): 
     # Return True if every space on the board has been taken. Otherwise, return False.
     for i in range(1, 10): 
         if isSpaceFree(board, i): # If variable "i" from 1 to 9 are all filled then return False. (XD)
             return False
     return True # returns True else wise. (XD)


print('Welcome to Tic-Tac-Toe!') #This is the "start" of the program. Everything up to this point has been defining functions that will be used throughout the course of the game (QW)

while True:
 # Reset the board.
 theBoard = [' '] * 10 #theBoard is a list of 10 empty spots (they're not actually empty, they still have the quotations but the quotations surround an empty spot) (QW)
 playerLetter, computerLetter = inputPlayerLetter() #Since inputPlayerLetter will return two values, the program assigns the users letter as the first value and the computers letter as the second (QW)
 turn = whoGoesFirst() #Calls the function used to randomly assign the start player. Line 130 informs the user who the assigned start player was.(QW)
 print('The ' + turn + ' will go first.')
 gameIsPlaying = True

 
 #
 # QUINN \/\/\/\/\/\/
 while gameIsPlaying:
  if turn == 'player':
   # Player's turn
   drawBoard(theBoard) #Draw out the board, empty at the start, then pieces will start to be filled by player/computer moves (QW)
   move = getPlayerMove(theBoard) #Get the move from the player (QW)
   makeMove(theBoard, playerLetter, move) #Draw the board according to the move (QW)

   if isWinner(theBoard, playerLetter): #check if the player won the game (QW)
    drawBoard(theBoard) #Draw out the final board(QW)
    print('Hooray! You have won the game!')
    gameIsPlaying = False #Stop the gameIsPlaying loop(QW)
   else:
    if isBoardFull(theBoard): #Check if the board is full, and thus a tie (QW)
     drawBoard(theBoard)
     print('The game is a tie!')
     break #Stop the loop, thus ending the game(QW)
    else:
     turn = 'computer' #If you haven't won or is the game a tie, pass the turn to the computer (QW)

  else:
   # Computer's turn
   #Everything below is a repeat of the previous code, just with the computers input and letter rather than the players (QW)
   move = getComputerMove(theBoard, computerLetter) #Calls the getComputerMove to get the computer move (wow!) (QW)
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
     turn = 'player' #Res
 print('Do you want to play again? (yes or no)') 
 if not input().lower().startswith('y'): #If no, run line 170. If yes, restart the loop and resume the game(QW)
  break #Breaks the while gameIsPlaying loop, this ending the game (QW)
  
  """print(" | |  |  | |  |  | | ")
print("-+-+- | -+-+- | -+-+-")
print(" | |  |  | |  |  | | ")
print("-+-+- | -+-+- | -+-+-")
print(" | |  |  | |  |  | | ")
print("******|*******|******")
print(" | |  |  | |  |  | | ")
print("-+-+- | -+-+- | -+-+-")
print(" | |  |  | |  |  | | ")
print("-+-+- | -+-+- | -+-+-")
print(" | |  |  | |  |  | | ")
print("******|*******|******")
print(" | |  |  | |  |  | | ")
print("-+-+- | -+-+- | -+-+-")
print(" | |  |  | |  |  | | ")
print("-+-+- | -+-+- | -+-+-")
print(" | |  |  | |  |  | | ")
print("******|*******|******")""" #just an idea for how to draw the bigger board

  
#gameOne = [" "]*10
#gameTwo = [" "]*10
#gameThree = [" "]*10
#gameFour = [" "]*10
#gameFive = [" "]*10
#gameSix = [" "]*10
#gameSeven = [" "]*10
#gameEight = [" "]*10
#gameNine = [" "]*10

#games = [gameOne,gameTwo,gameThree,gameFour,gameFive,fiveSix,fiveSeven,gameEight,gameNine] 
  
  #startGame will be the choice of the game that we start in
  #we are doing two player
  # moveOne is the move by player one
  # moveTwo is the move by player two
  
  #playerOneLetter
  #playerTwoLetter
  
  #1. print the game
  #2. print the game we're curruently playing in (RAY)
  
  
  #3. swap between games/play in the proper game (XIUWEN)
  
  
  #4. local win conditions (QUINN)
  #5. global win conditions
  
  
  #7. Starting the game -while game is playing loop (JOHN)
  
  
  
  
  #nextGame[moveOne] = playerOneLetter
  #nextGame = (moveOne-1) 
  
  #nextGame = 5
  #moveOne from player 
  #play moveOne in nextGame - games[nextGame-1][moveOne] = playerOneLetter 
  #change game - nextGame
  
  #moveTwo from player2
  #play moveTwo in nextGame
  #change game - reassign nextGame
  
  #moveOne from player 1
  #play moveOne in nextGame
  #ghange game - reassign nextGame
  
  
  #isWinner(games[4],playerOneLetter)
 
    
    
    
    
    
    
    
