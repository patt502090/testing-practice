from productions.cat_and_mouse import catAndMouse
import unittest

class TestCatAndMouseFunction(unittest.TestCase):

    def test_cat_and_mouse_cat_b_cat_a_mouse_far_away(self):
        result = catAndMouse(1, 3, 2)
        self.assertEqual(result, 'Mouse C')

    def test_cat_and_mouse_cat_b_catches(self):
        result = catAndMouse(1, 2, 3)
        self.assertEqual(result, 'Cat B')
        
    def test_cat_and_mouse_cat_b_cat_a_mouse_far_away(self):
        result = catAndMouse(1, 3, 2)
        self.assertEqual(result, 'Mouse C')

    def test_cat_and_mouse_cat_b_catches(self):
        result = catAndMouse(1, 2, 3)
        self.assertEqual(result, 'Cat B')

    def test_catA_catB_mouseC_catB_catches(self):
        result = catAndMouse(8, 5, -5)
        self.assertEqual(result, "Cat B")
        
    def test_catA_catB_mouseC_mouse_caught(self):
        result = catAndMouse(3, 3, 7)
        self.assertEqual(result, "Mouse C")
        
    def test_catA_catB_mouseC_catA_catches(self):
        result = catAndMouse(6, 7, 5)
        self.assertEqual(result, "Cat A")
        
    def test_catA_catB_mouseC_catB_catches(self):
        result = catAndMouse(7, 8, 9)
        self.assertEqual(result, "Cat B")






