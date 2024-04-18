def printBoard(Board):
    print(Board['Top-left'],"|", Board['Top-mid'],"|",Board['Top-right'],"|")
    print(Board['mid-left'],"|", Board['mid-mid'],"|",Board['mid-right'],"|")
    print(Board['down-left'],"|", Board['down-mid'],"|",Board['down-right'],"|")
    
Board = {
    "Top-left":" ","Top-mid":" ","Top-right":" ","mid-left":" ","mid-mid":" ","mid-right":" ","down-left":" ","down-mid":" ","down-right":" "
}
win_combo = [["Top-left","Top-mid","Top-right"],
             ["Top-left","mid-left","down-left"],
             ["Top-left","mid-mid","down-right"],
             ["mid-left","mid-mid","mid-right"],
             ["down-left","down-mid","down-right"],
             ["Top-mid","mid-mid","down-mid"],
             ["Top-right","mid-right","down-right"],
             ["Top-right","mid-mid","down-left"]]
current_turn = 'X'
def change_turn(current_turn):
    if current_turn=='X':
        play('O')
    elif current_turn=='O':
        play('X')
    
def check_win(cur):
    for i in win_combo:
        if Board[i[0]]==Board[i[1]]==Board[i[2]]==cur:
            return 'True'
    return False
def play(current_turn):
    pos = input("Enter position:")
    if pos not in Board or Board[pos]!= " ":
        print("Invalid")
        play(current_turn)
    else:
        Board[pos] = current_turn
        printBoard(Board)
        if check_win(current_turn):
            print(current_turn,"won")
        else:
            change_turn(current_turn)
            
play("X")   
printBoard(Board)
