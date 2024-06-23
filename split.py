import random
import math
import unittest

def split(items, ratios):
    if not math.isclose(sum(ratios), 1.0):
        raise ValueError("Total sum of the ratios must be 1.")
    
    total_items = len(items)
    sizes = [] 
    for ratio in ratios:
        size = math.ceil(ratio * total_items)
        sizes.append(size) 
    while sum(sizes) > total_items:
        max_index = sizes.index(max(sizes))
        sizes[max_index] -= 1
    
    random.shuffle(items)    
    result = []
    current_index = 0
    for size in sizes:
        result.append(items[current_index:current_index + size])
        current_index += size    
    return result

#test cases


class TestSplitFunction(unittest.TestCase):

    def test_split_basic(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ratios = [0.5, 0.4, 0.1]
        result = split(items, ratios)
        sizes = [len(part) for part in result]
        self.assertEqual(sizes, [5, 4, 1])
        self.assertEqual(sum(sizes), len(items))
        self.assertCountEqual(items, [item for sublist in result for item in sublist])

    def test_split_equal_ratios(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ratios = [0.25, 0.5, 0.25]
        result = split(items, ratios)
        sizes = [len(part) for part in result]
        self.assertEqual(sizes, [3, 4, 3])
        self.assertEqual(sum(sizes), len(items))
        self.assertCountEqual(items, [item for sublist in result for item in sublist])

    def test_split_different_ratios(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ratios = [0.1, 0.2, 0.3, 0.4]
        result = split(items, ratios)
        sizes = [len(part) for part in result]
        self.assertEqual(sizes, [1, 2, 3, 4])
        self.assertEqual(sum(sizes), len(items))
        self.assertCountEqual(items, [item for sublist in result for item in sublist])

    def test_split_zero_items(self):
        items = []
        ratios = [0.5, 0.5]
        result = split(items, ratios)
        sizes = [len(part) for part in result]
        self.assertEqual(sizes, [0, 0])
        self.assertEqual(sum(sizes), len(items))

    def test_split_invalid_ratios(self):
        items = [1, 2, 3, 4, 5]
        ratios = [0.5, 0.3, 0.3]
        with self.assertRaises(ValueError):
            split(items, ratios)

if __name__ == '__main__':
    unittest.main()
