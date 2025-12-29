board = ['1', '2', '3', '4', '5', '6','7', '8', '9']
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for i in range(0, 9, 3):
            print(f"+-------+-------+-------+")
            print(f"|       |       |       |")
            print(f"|   {board[i]}   |   {board[i+1]}   |   {board[i+2]}   |")
            print(f"|       |       |       |")
    print(f"+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        Player = int(input("Insere a Posiçao de 1-9"))
        Escolha = Player - 1
        if 0 < Player < 10:
            if board[Escolha] != 'X' and board[Escolha] != 'O':
                board[Escolha] = 'O'
                break
            else: 
                 print("Posição já preenchida!")
                 print()

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    List = []
    for i in range(9):    
        if board[i] != 'O' and board[i] != 'X':
            List.append((i))
    return List
    
while True:
    display_board(board)            
    enter_move(board)
    make_list_of_free_fields(board)




#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
                                                                                                                                                                                                                                                                                                                                                       

#def draw_move(board):
    # The function draws the computer's move and updates the board.
