from model import find_set
import random
from math import floor
from copy import deepcopy

# create a random board of traditional set gameplay (p=4, v=3). Returns the cards_on_board
def create_random_board_traditional_set():
    cards_on_board = [[]]
    num_properties = 4
    num_values = 3

    # generate all possible cards... in this case of traditional set this is 81 cards (3 ** 4)
    for p in range(num_properties):
        for c in range(len(cards_on_board)):
            card_to_expand = deepcopy(cards_on_board[c])
            for v in range(num_values):
                values = [0] * num_values
                values[v] = 1
                if(v == 0):
                    cards_on_board[c] += [values]
                else:
                    nc = card_to_expand + [values]
                    cards_on_board += [nc]

    # some basic sizing assertions against the cards that we have generated
    assert len(cards_on_board) == num_values ** num_properties 
    for c in range(len(cards_on_board)):
        assert len(cards_on_board[c]) == num_properties
        for p in range(len(cards_on_board[c])):
            assert len(cards_on_board[c][p]) == num_values
    
    # it has been proven that 21 cards must always contain a valid set in traditional gameplay
    return random.sample(cards_on_board, k=24)
create_random_board_traditional_set()

# given a set that our solver finds, make sure that it is actually valid
def assert_valid_set(cards_on_board, result, num_properties, num_values): 
    # solution has been found
    assert (len(result)) != 0

    # select the cards from the output of the solver
    cards_in_set = []
    for i, _ in enumerate(cards_on_board):
        if(result[i]):
            cards_in_set += [cards_on_board[i]]

    # number of cards must be the number of values
    assert len(cards_in_set) == num_values
    
    # enumerate every property
    for p in range(num_properties):
        # all values must be the same
        if(cards_in_set[0][p] == cards_in_set[1][p]):
            for c1 in range(num_values):
                for c2 in range(num_values):
                    if c1 != c2:
                        assert cards_in_set[c1][p] == cards_in_set[c2][p]
        # all values must be different
        else:
            for c1 in range(num_values):
                for c2 in range(num_values):
                    if c1 != c2:
                        assert cards_in_set[c1][p] != cards_in_set[c2][p]

# a (p=2, v=2) board should always have a valid set with 2 cards
def test_small_board_match_different():
    num_properties = 2
    num_values = 2
    cards_on_board = [
        [[0, 1], [1, 0]],
        [[1, 0], [0, 1]],
    ]
    result = find_set(cards_on_board, num_properties, num_values)

    assert result[0] == 1
    assert result[1] == 1

# a (p=2, v=2) board should always have a valid set with 2 cards
def test_small_board_match_same():
    num_properties = 2
    num_values = 2
    cards_on_board = [
        [[1, 0], [1, 0]],
        [[1, 0], [1, 0]],
    ]
    result = find_set(cards_on_board, num_properties, num_values)

    assert result[0] == 1
    assert result[1] == 1

# run finding a valid set on a traditional board in which we know sets exists and make sure we find one
def test_stress_test_traditional_set():
    iterations = 1000
    for i in range(iterations):
        cards_on_board = create_random_board_traditional_set()
        num_properties = 4
        num_values = 3
        result = find_set(cards_on_board, num_properties, num_values)

        # make sure that the result is valid
        assert_valid_set(cards_on_board, result, num_properties, num_values)
