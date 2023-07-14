
#Merge sort
#worst/average time complexity: \mathcal{O}(n \log n).
#Best time complexity: \mathcal{O}(n).


import unittest

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(input_z):
    if len(input_z) <= 1:
        return input_z

    mid = len(input_z) // 2
    left = input_z[:mid]
    right = input_z[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

class SortedTest(unittest.TestCase):

    def test_sorted(self):
        self.assertTrue(is_sorted([]))
        self.assertTrue(is_sorted([5]))
        self.assertFalse(is_sorted([6, 9, 8]))

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

if __name__ == '__main__':
    unittest.main()
