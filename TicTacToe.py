# Python Tic Tac Toe

game_row1 = ["A0","A1","A2"]
game_row2 = ["B0","B1","B2"]
game_row3 = ["C0","C1","C2"]


def display(row1,row2,row3):
    """
    Display function to show game board
    """
    pass
    print(row1)
    print(row2)
    print(row3)

def user_pick():
    row_pick = ''
    acceptable_range = range(0,3)
    within_range = False
    """
    User X or O choice
    """
    pass
    while row_pick.isdigit() == False or within_range==False:
        row_pick = input("Please make a choice (0-2): ")

        if row_pick.isdigit() == False:
            print("Sorry that choice is not a digit")

        if row_pick.isdigit() == True:
            if int(row_pick) in acceptable_range:
                within_range = True
            else:
                within_range_range = False
                print("Sorry that number is not in range")

    return int(row_pick)

def game_update(p,r1,r2,r3):
    """
    Updates gameboard with user pick
    """
    pass




display(game_row1, game_row2, game_row3)
user_pick()
# game_update(pick,game_row1, game_row2, game_row3)