from mip import *

"""
    Citation: I generalized the mathmatical formulation here (https://tommyodland.com/articles/2019/the-card-game-set-as-a-binary-integer-program/).
    into a parameterized model (the source hardcoded p=4 and v=3 see writeup for notation). The MIP library was used for implementation.
"""


"""
    Finds a valid Set on a board 

    A card is represented by a number[p][v] telling if a value is present (1) or not (0) for every property.

    @param cards_on_board: a list of cards that are currently on the board (number[][][])
    @param num_properties: the total number of properties for each card (number)
    @param num:values: the total number of possible values for each property (number)

    @returns number[]: a binary list of whether a card at index from cards_on_board is part of the solution or not
                       may return empty list if no solution is found
"""
def find_set(cards_on_board, num_properties, num_values):
    m = Model()

    # Descision variables representing whether to include a given card on the board or not
    include = [ m.add_var(var_type=BINARY) for i in range(len(cards_on_board)) ]

    # Must include exactly enough cards to form a valid Set
    m += xsum(include[i] for i in range(len(cards_on_board))) == num_values
    m.objective = maximize(xsum(include[i] for i in range(len(cards_on_board))))


    for p in range(num_properties):
        vsums = [xsum(include[i] * cards_on_board[i][p][v] for i in range(len(cards_on_board))) for v in range(num_values)]

        # use y binary variable to branch on whether all values are different or not
        y = m.add_var(var_type=BINARY)

        # use z binary variable to represent for each possible value if all cards have that value
        z =  [ m.add_var(var_type=BINARY) for i in range(num_values) ]

        # at most one z value can be true and one value is true if and only if y is false
        m += xsum(z[i] for i in range(num_values)) == 1 - y
        
        # a valid set is formed on the condition that all values for every property are either all the same or all different
        for i, _ in enumerate(vsums):
            m += vsums[i] == y + num_properties * z[i]

    m.verbose = 1
    status = m.optimize(max_seconds=100)

    if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
        return [round(v.x) for v in include]
    return []