#Algoritmos Minimax

def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_possible_moves(board):
            eval = minimax(make_move(board, move, 'X'), depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(board):
            eval = minimax(make_move(board, move, 'O'), depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_possible_moves(board):
    # Obtener las posibles jugadas en el tablero
    pass

def make_move(board, move, player):
    # Realizar una jugada en el tablero
    pass

def game_over(board):
    # Verificar si el juego ha terminado
    pass

def evaluate(board):
    # Evaluar el estado del tablero
    pass
