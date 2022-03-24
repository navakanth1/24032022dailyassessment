import unittest


def even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def prime(x):
    for i in range(2, x):
        if (x%i == 0):
            return "noprime"
            break
        else:
            return "prime"



def divisible(a):
    if a % 7 == 0:
        return True
    else:
        return False


class Singlenumbers(unittest.TestCase):
    def test_case_even(self):
        result = even(4)
        self.assertTrue(result)

    def test_case_odd(self):
        result = even(7)
        self.assertFalse(result)

    def test_case_prime(self):
        result = prime(7)
        self.assertEqual(result, "prime")

    def test_case_prime1(self):
        a = 10
        result = prime(a)
        self.assertEqual(result, "noprime")

    def test_case_divide7(self):
        result = divisible(21)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()