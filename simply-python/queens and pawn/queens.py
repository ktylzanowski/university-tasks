import random


def generate_board():
    board = [[0 for _ in range(8)] for _ in range(8)]
    return board


def place_queens(board, k):
    queens = []
    for _ in range(k):
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        while board[row][col] == 'Q':
            row = random.randint(0, 7)
            col = random.randint(0, 7)
        board[row][col] = 'Q'
        queens.append((row, col))
    return queens


def place_pawn(board):
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    while board[row][col] == 'Q' or board[row][col] == 'P':
        row = random.randint(0, 7)
        col = random.randint(0, 7)
    board[row][col] = 'P'
    return row, col


def display_board(board):
    for row in board:
        for col in row:
            if col == 0:
                print(".", end=" ")
            elif col == "Q":
                print("Q", end=" ")
            else:
                print("P", end=" ")
        print()


def is_pawn_in_danger(queens, pawn):
    danger_queens = []
    for queen in queens:
        if queen[0] == pawn[0] or queen[1] == pawn[1] or abs(queen[0] - pawn[0]) == abs(queen[1] - pawn[1]):
            danger_queens.append(queen)
    return danger_queens


def display_in_danger(danger_queens, pawn):
    if len(danger_queens) > 0:
        print(f"Pawn in position {pawn[0] +1}, {pawn[1]+1} is attacked by queens in positions:")
        for queen_pos in danger_queens:
            print(f"- Queen in position {queen_pos[0] + 1}, {queen_pos[1] + 1}")
    else:
        print("The pawn is not attacked by any queen.")


if __name__ == '__main__':
    k = random.randint(1, 5)
    board = generate_board()
    queens = place_queens(board, k)
    pawn = place_pawn(board)
    display_board(board)
    danger = is_pawn_in_danger(queens, pawn)
    display_in_danger(danger, pawn)
    while True:
        print("\n What you would like to do?")
        print("1. Draw a new position for the pawn")
        print("2. Remove any queen")
        print("3. Re-verification of beating")
        print("4. End program")
        choice = input("Select the option (1/2/3/4): ")

        if choice == '1':
            board[pawn[0]][pawn[1]] = 0
            pawn = place_pawn(board)
            print(f"New pawn position {pawn[0] + 1}, {pawn[1] + 1}")
            display_board(board)

        elif choice == '2':
            if len(queens) == 0:
                print("No more queens")
            else:
                print("Queens positions:")
                while True:
                    for i, queen in enumerate(queens):
                        print(f"Queen {i + 1}: {queen}")

                    remove_choice = input("Select the number of the queen to be removed (1/2/3/4/5): ")
                    remove_choice = int(remove_choice)

                    if len(queens) >= remove_choice > 0:
                        removed_queen = queens.pop(remove_choice - 1)
                        board[removed_queen[0]][removed_queen[1]] = 0
                        print(f"Queen {remove_choice} on position {removed_queen} has been removed.")
                        display_board(board)
                        break

                    else:
                        print("Incorrect Queen number. Dial again.")

        elif choice == '3':
            danger = is_pawn_in_danger(queens, pawn)
            display_board(board)
            display_in_danger(danger, pawn)

        elif choice == '4':
            break

        else:
            print("Incorrect choice")
