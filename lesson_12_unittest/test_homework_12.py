from lesson_07.homework_07 import (
sum_numbers, calculate_average, reverse_string,
find_longest_word
)
#test 1-3  ------------------------------------------

def test_sum_numbers_positive():
    actual_result = sum_numbers(2, 3)
    expected_result = 5

    assert actual_result == expected_result

def test_sum_numbers_with_zero():
    actual_result = sum_numbers(10, 0)
    expected_result = 10

    assert actual_result == expected_result

def test_sum_numbers_negative():
    actual_result = sum_numbers(-10, -3)
    expected_result = -13

    assert actual_result == expected_result

#test 4-6  ---------------------------------------------

def test_calculate_average():
    actual_result = calculate_average(list(range(10)))
    expected_result = 4.5

    assert actual_result == expected_result

def test_calculate_average_one_number():
    actual_result = calculate_average([10])
    expected_result = 10

    assert actual_result == expected_result

def test_calculate_average_float_numbers():
    actual_result = calculate_average([1.5, 2.5])
    expected_result = 2.0

    assert actual_result == expected_result

#test 7-9  ---------------------------------------------

def test_reverse_string():
    actual_result = reverse_string("Roman!")
    expected_result = "!namoR"

    assert actual_result == expected_result

def test_reverse_string_empty():
    actual_result = reverse_string("")
    expected_result = ""

    assert actual_result == expected_result

def test_reverse_one_char():
    actual_result = reverse_string("A")
    expected_result = "A"

    assert actual_result == expected_result

#test 10-12  ---------------------------------------------

def test_find_longest_word():
    actual_result = find_longest_word(
        ["cat", "elephant", "dog"]
    )
    expected_result = "elephant"

    assert actual_result == expected_result

def test_find_longest_one_word():
    actual_result = find_longest_word(["cat"])
    expected_result = "cat"

    assert actual_result == expected_result

def test_find_longest_word_same_length():
    actual_result = find_longest_word(["cat", "dog", "pig"])
    expected_result = "cat"

    assert actual_result == expected_result