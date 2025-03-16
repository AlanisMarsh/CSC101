import data
import hw1
import unittest
import math


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        input = 'meow'
        expected = 2
        result = hw1.vowel_count(input)
        self.assertEqual(expected, result)

    def test_vowel_count2(self):
        input = 'mmmmm'
        expected = 0
        result = hw1.vowel_count(input)
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists1(self):
        input = [[1,2,3], [1,2], [1,2], [1,2,3]]
        expected = [[1,2], [1,2]]
        result = hw1.short_lists(input)
        self.assertEqual(expected, result)

    def test_short_lists2(self):
        input = [[1,2,3], [1,2,3], [1,1,2], [1,2,3]]
        expected = []
        result = hw1.short_lists(input)
        self.assertEqual(expected, result)

    def test_short_lists3(self):
        input = [[1,2], [1,2], [1,2], [1,2]]
        expected = [[1,2], [1,2], [1,2], [1,2]]
        result = hw1.short_lists(input)
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs1(self):
        input = [[1,2,3], [1,2], [1,2], [1,2,3]]
        expected = [[1,2,3], [1,2], [1,2], [1,2,3]]
        result = hw1.ascending_pairs(input)
        self.assertEqual(expected, result)

    def test_ascending_pairs2(self):
        input = [[3,1,2], [3,2], [9,2], [1,2,3]]
        expected = [[3,1,2], [2,3], [2,9], [1,2,3]]
        result = hw1.ascending_pairs(input)
        self.assertEqual(expected, result)

    def test_ascending_pairs3(self):
        input = []
        expected = []
        result = hw1.ascending_pairs(input)
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices1(self):
        input1 = data.Price(3,99)
        input2 = data.Price(4,99)
        expected = data.Price(8,98)
        result = hw1.add_prices(input1, input2)
        self.assertEqual(expected, result)

    def test_add_prices2(self):
        input1 = data.Price(1,50)
        input2 = data.Price(1,50)
        expected = data.Price(3,00)
        result = hw1.add_prices(input1, input2)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area1(self):
        input = data.Rectangle(data.Point(0,0), data.Point(1,1))
        expected = 1
        result = hw1.rectangle_area(input)
        self.assertEqual(expected, result)

    def test_rectangle_area2(self):
        input = data.Rectangle(data.Point(1,5), data.Point(5,2))
        expected = 12
        result = hw1.rectangle_area(input)
        self.assertEqual(expected, result)

    def test_rectangle_area3(self):
        input = data.Rectangle(data.Point(2,15), data.Point(12,5))
        expected = 100
        result = hw1.rectangle_area(input)
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author(self):
        input1 = 'Sarah J Maas'
        input2 = [data.Book(['Sarah J Maas'], 'Throne of Glass'),  data.Book(['JK Rowling'], 'Harry Potter'), data.Book(['Sarah J Maas'], 'A Court of Thorns and Roses')]
        expected = ['Throne of Glass', 'A Court of Thorns and Roses']
        result = hw1.books_by_author(input1, input2)
        self.assertEqual(expected, result)

    def test_books_by_author2(self):
        input1 = 'JK Rowling'
        input2 = [data.Book(['Sarah J Maas', 'JK Rowling'], 'Throne of Glass'),  data.Book(['JK Rowling'], 'Harry Potter'), data.Book(['Sarah J Maas'], 'A Court of Thorns and Roses')]
        expected = ['Throne of Glass', 'Harry Potter']
        result = hw1.books_by_author(input1, input2)
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound(self):
        input = data.Rectangle(data.Point(0,0), data.Point(1,1))
        expected = data.Circle(data.Point(0.5,0.5), 0.7071067811865476)
        result = hw1.circle_bound(input)
        self.assertEqual(expected, result)

    def test_circle_bound2(self):
        input = data.Rectangle(data.Point(-3.5,-5.0), data.Point(1,2))
        expected = data.Circle(data.Point(-1.25,-1.5), 4.16082924427331)
        result = hw1.circle_bound(input)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average(self):
        input = [data.Employee('lani', 1), data.Employee('naz', 15), data.Employee('ryan', 15), data.Employee('jess', 15)]
        expected = ['lani']
        result = hw1.below_pay_average(input)
        self.assertEqual(expected, result)

    def test_below_pay_average(self):
        input = [data.Employee('lani', 10), data.Employee('naz', 10), data.Employee('ryan', 5), data.Employee('jess', 15)]
        expected = ['ryan']
        result = hw1.below_pay_average(input)
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
