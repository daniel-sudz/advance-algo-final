from model import find_set


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
 
