import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def circletest(self):
        expected = task.CircleArea(1)
        self.assertEqual(expected, 3.14)


if __name__ == '__main__':
    unittest.main()
