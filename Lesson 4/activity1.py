import random
from colorama import init, Fore, Style
init(autoreset=True)

# =========================================
# CONSTANTS (DO NOT EDIT)
# =========================================
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]


# ==========================================================
# Display the Tic Tac Toe board's current state
# ==========================================================
def display_board(board):
    """Prints the Tic-Tac-Toe board in color."""
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()


# ==========================================================
# Initial choice of symbol given to player 
# ==========================================================
def player_choice():
    """Asks player to choose X or O and returns (player_symbol, ai_symbol)."""
    symbol = ''

    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).strip().upper()

    return ('X', 'O') if symbol == 'X' else ('O', 'X')


# ==========================================================
# Allows the player to make a move by choosing a number from 1 to 9
# ==========================================================
def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
        except ValueError:
            print("Please enter a number between 1 and 9")

    board[move - 1] = symbol


# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):
    # Case A: Check if AI can win in 1 move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return

    # Case B: Block the player's win in the next move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    
    # Case C: Random Move since no one is winning in the next move
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol


# ==========================================================
# Have any of the winning combinations been marked by a player?
# ==========================================================
def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # Horizontal

        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # Vertical

        (0, 4, 8), (2, 4, 6)                # Diagonal
    ]

    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True

    return False


# ==========================================================
# Determines whether there's no remaining moves
# ==========================================================
def check_full(board):
    return all(not spot.isdigit() for spot in board)


# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    # Ask player's name in green and store it
    # Hint: if empty, default to "Player"
    name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    if not name:
        name = 'Player'

    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Get symbols using player_choice()
        player_symbol, ai_symbol = player_choice()

        # Decide who starts ("Player" or "AI")
        # Simple option: always start with Player
        turn = name

        game_on = True

        while game_on:
            display_board(board)

            if turn == name:
                # Call player_move() to place player's symbol
                player_move(board, player_symbol)

                # If player wins, print win message with name and break
                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"Congratulations! {name}, you have won the game!")
                    game_on = False
                else:
                    # If tie (board full), print tie message and break
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        game_on = False
                    else:
                        # Switch turn to "AI"
                        turn = "AI"

            else:
                # Call ai_move() to place AI symbol
                ai_move(board, ai_symbol, player_symbol)

                # If AI wins, print AI win message and break
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                else:
                    # If tie (board full), print tie message and break
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        game_on = False
                    else:
                        # Switch turn to "Player"
                        turn = name

        # Ask "Play again? (yes/no): "
        play_again = input("Do you want to play again? (yes/no)").lower()
        # If answer is NOT "yes", print thank you and return
        if play_again != 'yes':
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    tic_tac_toe()