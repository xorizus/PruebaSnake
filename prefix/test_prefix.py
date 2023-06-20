import prefix
import unittest

def test_common_prefix():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 9, 10]
    result = prefix.common_prefix(list1, list2)
    assert result == [1, 2, 3] 

if __name__ == '__main__':
    unittest.main()