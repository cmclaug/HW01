import unittest

def classify_triangle(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        return "not a triangle"
    if (a*a + b*b == c*c):
        return "right triangle"
    if (a == b and b == c):
        return "equilateral triangle"
    if (a == b or b == c or a == c):
        return "isosceles triangle"
    return "scalene triangle"

class Test(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "right triangle")
        self.assertEqual(classify_triangle(4, 4, 5), "isosceles triangle")
        self.assertEqual(classify_triangle(4, 4, 4), "equilateral triangle")
        self.assertEqual(classify_triangle(3, 4, 6), "scalene triangle")
        self.assertEqual(classify_triangle(3, 4, 0), "not a triangle")
