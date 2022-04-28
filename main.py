'''
Tic-tac-toe game utils.

'''


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, position_x, position_y, player):
    # TODO: modificar tablero con nuevo movimiento del jugador en posicion indicada.

  board [position_y][position_x]=str(player)



    # P_2[0]
    # p_2[1]
    
    # board = create_b()
    # update_board(p_1, p_2, p_3)
    
    # return board

    # result = update_board(borad, [2, 0], "X")
    # boad = result

    # pass


def check_for_winner(board):
    # TODO: evaluar si el jugador indicado ha ganado la partida.

  
  
#Primera fila
  if board[0][0] and board[0][1] and board[0][2]:
      print("Ganó") 
      True
  
  #segunda fila
  if board[1][0] and board[1][1] and board[1][2]:
      print("Ganó")
      True
  
  #tercera fila
  if board[2][0] and board[2][1] and board[2][2]:
      print("Ganó")  
      True
  
  #primera columna
  if board[0][0] and board[1][0] and board[2][0]:
    print("Ganó")
    True
  
  #segunda columna
  if board[0][1] and board[1][1] and board[2][1]:
      print("Ganó")
      True
  
  #tercera columna
  if board[0][2] and board[1][2] and board[2][2]:
      print("Ganó")
      True
  
  #diagonal acendente
  if board[2][0] and board[1][1] and board[0][2]:
      print("Ganó")
      True
  
  #diagonal decendente
  if board[0][0] and board[1][1] and board[2][2]:
      print("Ganó")
      True
  
    
  return False


'''
Testing: 
'''
# board = create_empty_board()
# print_board(board)

winner = False
board = create_empty_board()
print_board(board)

while winner == False:

  position_x = int(input("Elejerir en X: "))
  position_y = int(input("Elejerir en Y: "))
  player = str(input("Jugar X/0..."))
  update_board(board, position_x, position_y, player)
  print_board(board)
  winner = check_for_winner(board)