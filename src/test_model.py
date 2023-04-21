from model import find_set
from copy import deepcopy
import random
import pytest

# create a random board of traditional set gameplay (p=4, v=3). Returns the cards_on_board
def create_random_board_traditional_set(num_properties, num_values, num_cards):
    cards_on_board = [[]]

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
    return random.sample(cards_on_board, k=num_cards)

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
# it is known that a valid set must exist when there are >= 21 cards on the board
def test_stress_test_traditional_set():
    iterations = 10000
    for i in range(iterations):
        cards_on_board = create_random_board_traditional_set(4, 3, 21)
        num_properties = 4
        num_values = 3
        result = find_set(cards_on_board, num_properties, num_values)

        # make sure that the result is valid
        assert_valid_set(cards_on_board, result, num_properties, num_values)

# probability breakdowns for finding a valid set below 21 cards:
# https://math.stackexchange.com/a/203146
# we can test our solver by making sure that a set is not found at some point for decks with 15 cards
# with 10000 iterations, the chance of not finding a set should be around 1 - ((0.99963531493045) ^ 10000) ~= 0.9739442246
# it should take a few minutes before the solver fails to find a valid set
def test_stress_traditional_set_no_set_found():
    with pytest.raises(Exception):
        while True:
            cards_on_board = create_random_board_traditional_set(4, 3, 15)
            num_properties = 4
            num_values = 3
            result = find_set(cards_on_board, num_properties, num_values)

            # make sure that the result is valid
            assert_valid_set(cards_on_board, result, num_properties, num_values)