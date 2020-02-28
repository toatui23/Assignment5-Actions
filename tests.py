import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = task.CircleArea(1)
        self.assertEqual(expected, 3.14)

    def test4(self):
          list = ['1', '2', '3', '4']
          first, last = task.firstandlast(list)
          self.assertEqual(first, list[0])
          self.assertEqual(last, list[-1])


if __name__ == '__main__':
    unittest.main()
