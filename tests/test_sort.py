import unittest
import random
import sort


class sort_Test(unittest.TestCase):

    randnums = []
    x = 1
    while (x < 11):
        y = (random.randrange(1, 100))
        randnums.append(y)
        x += 1

    num1 = [0,1,2,3,4,5,6,7,8,9]
    num2 = [5,6,2,3,7,8,9,1,4,0]


    def test_bubbleSort(self):
        res = sort.bubbleSort(self.num2)
        self.assertEqual(res, self.num1)


    def test_insertionSort(self):
        res = sort.insertionSort(self.num2)
        self.assertEqual(res, self.num1)


if __name__=='__main__':
    unittest.main()
