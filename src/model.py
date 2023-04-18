from mip import *




"""
    Finds a valid Set on a board 

    A card is represented by a number[] containing the value for each card property

    @param cards_on_board: a list of cards that are currently on the board (number[][])
    @param num_properties: the total number of properties for each card (number)
    @param num:values: the total number of possible values for each property (number)

    @returns number[][]: a list of cards that form a valid Set or empty list if none are found
"""
def find_set(cards_on_board, num_properties, num_values):
    m = Model()

    # Descision variables representing whether to include a given card on the board or not
    include = [ m.add_var(var_type=BINARY) for i in range(cards_on_board) ]

    # Must include exactly enough cards to form a valid Set
    m += xsum(include[i] for i in range(cards_on_board)) == num_properties


    for p in range(num_properties):
        vsums = [xsum(include[i] * cards_on_board[i][p][v] for i in range(cards_on_board)) for v in range(num_values)]

        # use y binary variable to branch on whether all values are the same or not
        y = m.add_var(var_type=BINARY)

        # use z binary variable to represent for each possible value if all cards have that value
        all_same_value =  [ m.add_var(var_type=BINARY) for i in range(num_values) ]

        


    #m.objective = maximize(xsum(include[i] for i in range(num_properties)))


    pass
