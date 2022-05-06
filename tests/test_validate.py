from unittest import TestCase

import validate

class TestValidate(TestCase):
    def test_is_odd_when_odd(self):
        self.assertEqual(validate.is_odd(1), True)

    def test_is_odd_when_even(self):
        self.assertEqual(validate.is_odd(2), False)

    def test_is_even_when_odd(self):
        self.assertEqual(validate.is_even(1), False)

    def test_is_even_when_even(self):
        self.assertEqual(validate.is_even(2), True)

    def test_is_between(self):
        self.assertEqual(validate.is_between(2, 1, 3), True)

    def test_is_between(self):
        self.assertEqual(validate.is_between(1, 2, 3), False)

    def test_is_outside(self):
        self.assertEqual(validate.is_outside(2, 1, 3), False)

    def test_is_outside(self):
        self.assertEqual(validate.is_outside(1, 2, 3), True)
