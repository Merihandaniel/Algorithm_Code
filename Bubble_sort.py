#worst/average time complexity: \mathcal{O}(n^2)
#Best time complexity: \mathcal{O}(n)

import unittest

def bubbleSort(input_y):
    n = len(input_y)

    for i in range(n):
        for j in range(0, n-i-1):
            if input_y[j] > input_y[j+1]:
                input_y[j], input_y[j+1] = input_y[j+1], input_y[j]

# Example:
input_y = [4, 9, 0, 6, 3]
bubbleSort(input_y)
print(input_y)


class BubbleSortTest(unittest.TestCase):

    def test_bubble_sort(self):
        input_y = [4, 9, 0, 6, 3]
        expected_result = [0, 3, 4, 6, 9]
        bubbleSort(input_y)
        self.assertEqual(input_y, expected_result)

if __name__ == '__main__':
    unittest.main()