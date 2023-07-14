#worst/average time complexity: \mathcal{O}(n^2)
#Best time complexity: \mathcal{O}(n)

import unittest

def insertionSort(input_x):
    for i in range(1, len(input_x)):
        key = input_x[i]
        j = i - 1
        while j >= 0 and key < input_x[j]:
            input_x[j + 1] = input_x[j]
            j -= 1
        input_x[j + 1] = key

# Example:
input_x = [10, 9, 8, 6, 3]
insertionSort(input_x)
print(input_x)


class InsertionSortTest(unittest.TestCase):

    def test_insertion_sort(self):
        input_x = [10, 9, 8, 6, 3]
        expected_result = [3, 6, 8, 9, 10]
        insertionSort(input_x)
        self.assertEqual(input_x, expected_result)

if __name__ == '__main__':
    unittest.main()