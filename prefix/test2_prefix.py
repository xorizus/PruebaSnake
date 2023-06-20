import prefix as pfx
def test_common_prefix():
    # Test case 1: Common prefix exists
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 9, 10]
    assert pfx.common_prefix(list1, list2) == [1, 2, 3]

    # Test case 2: Empty lists
    list3 = []
    list4 = []
    assert pfx.common_prefix(list3, list4) == []

    # Test case 3: No common prefix
    list5 = [1, 2, 3, 4, 5]
    list6 = [6, 7, 8, 9, 10]
    assert pfx.common_prefix(list5, list6) == []

    # Test case 4: One empty list
    list7 = [1, 2, 3, 4, 5]
    list8 = []
    assert pfx.common_prefix(list7, list8) == []

    # Test case 5: Lists of different lengths
    list9 = [1, 2, 3]
    list10 = [1, 2, 3, 4, 5]
    assert pfx.common_prefix(list9, list10) == [1, 2, 3]

    print("All tests passed!")

# Run the unit tests
test_common_prefix()