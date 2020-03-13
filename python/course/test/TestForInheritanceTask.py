import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

import python.course.stepik.TaskFromStepikInheritance as inheritance_proj


class TestUM(unittest.TestCase):
    test_input_for_test_inheritance_1 = [
        "4",
        "A",
        "B : A",
        "C : A",
        "D : B C",
        "4",
        "A B",
        "B D",
        "C D",
        "D A"
    ]

    def test_example(self):
        self.assertEqual(3 * 4, 12)

    @patch('builtins.input', MagicMock(side_effect=test_input_for_test_inheritance_1))
    def test_inheritance(self):
        expected = [
            "Yes",
            "Yes",
            "Yes",
            "No"
        ]
        inheritance_proj.enterInputValues()
        actual = inheritance_proj.search_parents_of_classes()
        self.assertListEqual(expected, actual)
