# Python Tic Tac Toe

game_row1 = ["","",""]
game_row2 = ["","",""]
game_row3 = ["","",""]


def display(row1,row2,row3):
    """
    Display function to show game board
    """
    pass
    print(f"{row1}\n{row2}\n{row3}")

def userrow_pick():
    row_pick = ''
    acceptable_range = range(0,3)
    within_range = False
    """
    User X or O choice
    """
    pass
    while row_pick.isdigit() == False or within_range==False:
        row_pick = input("Please choose a row (0-2): ")

        if row_pick.isdigit() == False:
            print("Sorry that choice is not a digit")

        if row_pick.isdigit() == True:
            if int(row_pick) in acceptable_range:
                within_range = True
            else:
                within_range_range = False
                print("Sorry that number is not in range")

    return int(row_pick)

def userindex_pick():
    index_pick = ''
    acceptable_range = range(0,3)
    within_range = False
    """
    User X or O choice
    """
    pass
    while index_pick.isdigit() == False or within_range==False:
        index_pick = input("Please choose a space (0-2): ")

        if index_pick.isdigit() == False:
            print("Sorry that choice is not a digit")

        if index_pick.isdigit() == True:
            if int(row_pick) in acceptable_range:
                within_range = True
            else:
                within_range_range = False
                print("Sorry that number is not in range")

    return int(index_pick)

def game_update(p,i,r1,r2,r3):
    """
    Updates gameboard with user pick
    """
    
    pass
    if p == 0:
        r1[i] = "X"
        display(r1,r2,r3)
    elif p == 1:
        r2[i] = "X"
        display(r1,r2,r3)
    elif p == 2:
        r3[i] = "X"
        display(r1,r2,r3)
    else:
        pass


display(game_row1, game_row2, game_row3)
row_pick = userrow_pick()
index_pick = userindex_pick()
game_update(row_pick, index_pick, game_row1, game_row2, game_row3)
