board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_move(player):
    while True:
        try:
            choice = int(input(f"player {player}, enter your choice: "))
        except ValueError:
            print("Please enter a number")
            continue
        if choice < 1 or choice > 9:
            continue
        row = (choice - 1) // 3
        col = (choice - 1) % 3
        if board[row][col] != "":
            print("this spot is already taken")
            continue
        return row, col
while True:
    game_over = False
    while not game_over:
        print_board(board)

        winning_lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
                ]
        row, col = get_move('X')
        board[row][col] = "X"
        print_board(board)
        for line in winning_lines:
            if all(board[row][col] == 'X' for row, col in line):
                print('X win')
                game_over = True
                break
        if not game_over:
            row, col = get_move('O')
            board[row][col] = "O"
            print_board(board)
            for line in winning_lines:
                if all(board[row][col] == 'O' for row, col in line):
                    print('O win')
                    game_over = True
                    break
        if not game_over:
            if all(board[row][col] == '' for row in range(3) for col in range(3)):
                print('Tie')
                game_over = True
                break


    again = input("Do you want to play again? (y/n): ")
    if again == 'y':
        board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
    else:
        print("Thank you for playing")
        break





