player,opponent = 'X','O'

def isMovesLeft(board):
    for row in board:
        if '_' in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            if row[0] == player:
                return 10
            elif row[0] == opponent:
                return -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]!='_':
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10
    return 0

def minimax(board,depth,isMax):
    score = evaluate(board)
    if score == 10:
        return score
    if score == -10:
        return score
    if not isMovesLeft(board):
        return 0
    
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best,minimax(board,depth+1,not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best,minimax(board,depth+1,not isMax))
                    board[i][j] = '_'
        return best
    
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board,0,False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestVal = moveVal
                    bestMove = (i,j)
    return bestMove

def printBoard(board):
    for row in board:
        print(' '.join(row))
    print()

if __name__ == "__main__":
    board = [
        ['X','O','X'],
        ['O','O','X'],
        ['_','_','_'],
    ]
    print("Original Board");
    printBoard(board);
    bestMove = findBestMove(board)  
    print("The Best Move is Row :",bestMove[0]," Col : ",bestMove[1])
    
    