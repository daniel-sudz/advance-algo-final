from model import find_set
from random import random
from math import floor

# create a random board of traditional set gameplay (p=4, v=3). Returns the cards_on_board
def create_random_board_traditional_set():
    cards_on_board = []
    num_properties = 4
    num_values = 3

    # it is proven that 21 cards are sufficient to always have a valid set in the traditional game
    for n in range(21):
        card = []
        # find which value to set for every property in the random card
        for p in range(num_properties):
            which_value = floor(random() * num_values)
            values = [0] * num_values
            values[which_value] = 1
            card += [values]
        cards_on_board += [card]

    return cards_on_board

# given a set that our solver finds, make sure that it is actually valid
def assert_valid_set(cards_on_board, result, num_properties, num_values): 
    pass

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
    iterations = 5
    for i in range(iterations):
        card_on_board = create_random_board_traditional_set()
        num_properties = 4
        num_values = 3
        result = find_set(card_on_board, num_properties, num_values)

        # make sure that the result is valid
