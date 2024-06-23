import unittest
from statistics import read_data, calculate_statistics

class TestStatistics(unittest.TestCase):

    def test_read_data(self):
        test_data = [
            ['Belgium', 'BEL', '2010', '8.29'],
            ['Belgium', 'BEL', '2011', '7.50'],
            ['Germany', 'DEU', '2010', '5.60'],
            ['Belgium', 'BEL', '2012', '6.80'],
            ['Germany', 'DEU', '2011', '5.70'],
        ]
        
        with open('test_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(test_data)
        
        data = read_data('test_data.csv', 'Belgium', None, None)
        self.assertEqual(data, [8.29, 7.5, 6.8])
        
        data = read_data('test_data.csv', 'Belgium', 2011, None)
        self.assertEqual(data, [7.5, 6.8])
        
        data = read_data('test_data.csv', 'Belgium', None, 2011)
        self.assertEqual(data, [8.29, 7.5])
        
        data = read_data('test_data.csv', 'Belgium', 2011, 2011)
        self.assertEqual(data, [7.5])

    def test_calculate_statistics(self):
        data = [8.29, 7.5, 6.8]
        self.assertAlmostEqual(calculate_statistics(data, 'avg'), 7.53, places=2)
        self.assertEqual(calculate_statistics(data, 'min'), 6.8)
        self.assertEqual(calculate_statistics(data, 'max'), 8.29)
        
        with self.assertRaises(ValueError):
            calculate_statistics([], 'avg')

if __name__ == '__main__':
    unittest.main()
