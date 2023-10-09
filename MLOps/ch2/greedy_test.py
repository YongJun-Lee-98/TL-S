import change
import unittest

class TestChange(unittest.TestCase):
    def test_get_c500(self):
        alg = change.Algorithm(5000, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 10)
        self.assertEqual(c100, 0)
        self.assertEqual(c50, 0)
        self.assertEqual(c10, 0)
    def test_get_c500(self):
        alg = change.Algorithm(200, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 0)
        self.assertEqual(c100, 2)
        self.assertEqual(c50, 0)
        self.assertEqual(c10, 0)
    def test_get_c500(self):
        alg = change.Algorithm(50, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 0)
        self.assertEqual(c100, 0)
        self.assertEqual(c50, 1)
        self.assertEqual(c10, 0)
    def test_get_c500(self):
        alg = change.Algorithm(40, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 0)
        self.assertEqual(c100, 0)
        self.assertEqual(c50, 0)
        self.assertEqual(c10, 4)
    def test_get_c500(self):
        alg = change.Algorithm(4290, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 8)
        self.assertEqual(c100, 2)
        self.assertEqual(c50, 1)
        self.assertEqual(c10, 4)
if __name__ == "__main__":
    unittest.main()      