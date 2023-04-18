from mip import *

"""
    Citation: I generalized the mathmatical formulation here (https://tommyodland.com/articles/2019/the-card-game-set-as-a-binary-integer-program/).
    into a parameterized model (the source hardcoded p=3 and v=4 see writeup for notation). The MIP library was used for implementation.
"""


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
    include = [ m.add_var(var_type=BINARY) for i in range(len(cards_on_board)) ]

    # Must include exactly enough cards to form a valid Set
    m += xsum(include[i] for i in range(len(cards_on_board))) == num_properties


    for p in range(num_properties):
        vsums = [xsum(include[i] * cards_on_board[i][p][v] for i in range(len(cards_on_board))) for v in range(num_values)]

        # use y binary variable to branch on whether all values are different or not
        y = m.add_var(var_type=BINARY)

        # use z binary variable to represent for each possible value if all cards have that value
        z =  [ m.add_var(var_type=BINARY) for i in range(num_values) ]

        # at most one z value can be true and one value is true if and only if y is false
        m += xsum(z[i] for i in range(num_values)) == 1 - y
        
        # if y is true, 
        for i, _ in enumerate(vsums):
            m += vsums[i] == y + num_properties * z[i]
    
    status = m.optimize(max_seconds=10)


# Run the solver on a traditional version of Set and an example board
def example_find():
    cards_on_board = [
        [[0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]], # card 1
        [[0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]], # card 2
        [[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], # card 3
        [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]], # card 4
        [[0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0]], # card 5
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]], # card 6
        [[0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]], # card 7
        [[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]], # card 8
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], # card 9
        [[1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0]], # card 10
        [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0]], # card 11
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]], # card 12
    ],
    num_properties = 3 
    num_values = 4
    find_set(cards_on_board, num_properties, num_values)

example_find()