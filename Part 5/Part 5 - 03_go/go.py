def who_won(game_board: list):

    player1_count = 0
    player2_count = 0

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                player1_count += 1
            elif game_board[i][j] == 2:
                player2_count += 1

    if player1_count > player2_count:
        return 1
    elif player1_count < player2_count:
        return 2
    else:
        return 0
    
if __name__ == "__main__":
    go_array = int(input("Type the score"))

    who_won(go_array)