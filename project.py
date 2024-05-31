import random
from time import sleep
from queue import Queue

def main():
    arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = player_xo()

    player_queue = Queue(maxsize = 3)
    computer_queue = Queue(maxsize = 3)
    player_start_first = True
    win = False

    if player == "X":
        player_start_first = False
        computer = "O"
    else:
        computer = "X"

    while not win:
        if player_start_first:
            sleep(1)
            print("\nPlayer Turns!\n")
            arr = player_plays(arr, player, player_queue)
            player_start_first = False 
        else:
            # Computer turn
            sleep(1)
            print("\nComputer's Turn!\n")
            arr = computer_plays(arr, computer, computer_queue)
            if check_win(arr, player):
                print_board(arr)
                print("\nPlayer wins!\n")
                break

            # Player turn
            sleep(1)
            print("\nPlayer's Turn!\n")
            arr = player_plays(arr, player, player_queue)
            if check_win(arr, player):
                print_board(arr)
                print("\nPlayer wins!\n")
                break

def check_win(arr, player):
    return row_win(arr, player) or col_win(arr, player) or diag_win(arr, player)

def row_win(arr, player):
    for i in range(0, 9, 3):
        if arr[i] == arr[i+1] == arr[i+2] == player:
            return True
    return False

def col_win(arr, player):
    for i in range(3):
        if arr[i] == arr[i+3] == arr[i+6] == player:
            return True
    return False

def diag_win(arr, player):
    if arr[0] == arr[4] == arr[8] == player or arr[2] == arr[4] == arr[6] == player:
        return True
    return False

def player_plays(arr, player, q):
    print_board(arr)

    if q.full():
        relocate = int(q.get()) - 1 # get element from queue and chage to arr position
        print("\nYou will relocate " +  player + " from tile " + str(relocate+1) + " to a new tile\n")
        player_input = str(input("\nchoose a valid tile, which is numbered: "))
        if is_valid_tile(player_input, arr):
            arr[int(player_input)-1] = player
            arr[relocate] = str(relocate+1) # remove the previous tile
            q.put(player_input)
        else:
            print("\nInvalid tiles! Please choose the numbered tiles\n")
            arr = player_plays(arr, player,q)
    else:
        player_input = str(input("\nchoose a valid tile, which is numbered: "))
        if is_valid_tile(player_input, arr):
            arr[int(player_input)-1] = player
            q.put(player_input)
        else:
            print("\nInvalid tiles! Please choose the numbered tiles\n")
            arr = player_plays(arr, player, q)
    return arr

def computer_plays(arr, computer, q):
    while True:
        computer_input = random.choice(arr)
        if computer_input != "X" and computer_input != "O":
            break

    if q.full():
        relocate = int(q.get()) - 1
        print("Computer relocate " +  computer + " from tile " + str(relocate+1) + " to tile " + computer_input + "\n")
        arr[int(computer_input)-1] = computer
        arr[relocate] = str(relocate+1)
        q.put(computer_input)
    else:
        print("Computer Choose Tile " + computer_input + "\n")
        arr[int(computer_input)-1] = computer
        q.put(computer_input)
    return arr

def is_valid_tile(input, arr):
    # check if input is in tile is number
    if arr[int(input)-1] == "X" or arr[int(input)-1] == "O":
        return False
    return True

def print_board(arr):
    print(f"{arr[0]} | {arr[1]} | {arr[2]}")
    print("--+---+--")
    print(f"{arr[3]} | {arr[4]} | {arr[5]}")
    print("--+---+--")
    print(f"{arr[6]} | {arr[7]} | {arr[8]}")

def player_xo():
    print("\n'O' goes first, 'X' goes second.\n")
    player = str(input("Choose X or O :"))
    if player == "X" or player == "x":
        print("Player is X")
        print("Computer is O")
    elif player == "O" or player == "o":
        print("Player is O")
        print("Computer is X")
    else:
        print("Invalid input. Please try again.")
        player = player_xo()
    return player.upper()


if __name__ == "__main__":
    main()