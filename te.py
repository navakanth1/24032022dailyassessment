import unittest
def add(x,y):
    return x+y
def add1(x,y,z):
    return x+y+z
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
class Operations(unittest.TestCase):
    def test_case_add(self):
        a = 5
        b = 78
        result = add(a,b)
        self.assertEqual(result,a+b)
    def test_case_add1(self):
        a = 65
        b = 47
        c = 78
        result = add1(a,b,c)
        self.assertEqual(result,a+b+c)
    def test_case_sub(self):
        a = 54
        b = 45.4
        result =  sub(a,b)
        self.assertEqual(result,a-b)
    def test_case_multi(self):
        f = 457
        h = 457
        result = mul(f,h)
        self.assertEqual(result,f*h)
    def test_case_division(self):
        h = 457
        p = 47
        result = div(h,p)
        self.assertEqual(result,h/p)

if __name__ == "__main__":
    unittest.main()