#Algoritmos Alpha-Beta Pruning

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_possible_moves(board):
            eval = alpha_beta_pruning(make_move(board, move, 'X'), depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(board):
            eval = alpha_beta_pruning(make_move(board, move, 'O'), depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
