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

    test_input_for_test_inheritance_2 = [
        "10",
        "classA : classB classC classD classG classH",
        "classB : classC classE classG classH classK classL",
        "classC : classE classD classH classK classL",
        "classE : classD classF classK classL",
        "classD : classG classH",
        "classF : classK",
        "classG : classF",
        "classH : classL",
        "classK : classH classL",
        "classL",
        "38",
        "classK classD",
        "classD classA",
        "classG classD",
        "classH classA",
        "classE classE",
        "classH classG",
        "classE classL",
        "classB classD",
        "classD classL",
        "classD classG",
        "classD classE",
        "classA classF",
        "classA classC",
        "classK classA",
        "classA classH",
        "classK classD",
        "classH classB",
        "classK classB",
        "classD classL",
        "classG classG",
        "classA classH",
        "classK classL",
        "classG classE",
        "classB classA",
        "classC classK",
        "classK classL",
        "classC classL",
        "classG classC",
        "classD classD",
        "classC classG",
        "classE classA",
        "classF classK",
        "classB classG",
        "classH classL",
        "classL classF",
        "classH classG",
        "classD classA",
        "classH classL"
    ]

    def test_example(self):
        self.assertEqual(3 * 4, 12)

    @patch('builtins.input', MagicMock(side_effect=test_input_for_test_inheritance_1))
    def test_inheritance_1(self):
        expected = [
            "Yes",
            "Yes",
            "Yes",
            "No"
        ]
        inheritance_proj.enterInputValues()
        actual = inheritance_proj.search_parents_of_classes()
        self.assertListEqual(expected, actual)

    @patch('builtins.input', MagicMock(side_effect=test_input_for_test_inheritance_2))
    def test_inheritance_2(self):
        expected = [
            "Yes",
            "Yes",
            "Yes",
            "Yes",
            "Yes",
            "Yes",
            "No",
            "No",
            "No",
            "No",
            "Yes",
            "No",
            "No",
            "Yes",
            "No",
            "Yes",
            "Yes",
            "Yes",
            "No",
            "Yes",
            "No",
            "No",
            "Yes",
            "Yes",
            "No",
            "No",
            "No",
            "Yes",
            "Yes",
            "No",
            "Yes",
            "No",
            "No",
            "No",
            "Yes",
            "Yes",
            "Yes",
            "No"
        ]
        inheritance_proj.enterInputValues()
        actual = inheritance_proj.search_parents_of_classes()
        self.assertListEqual(expected, actual)
