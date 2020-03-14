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

    test_input_for_test_inheritance_3 = [
        "2",

        "A : C B",

        "B : D E",

        "1",

        "E A"
    ]

    test_input_for_test_inheritance_4 = [  # список введённых строк
        '12',
        'G : F',
        # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
        'A',
        'B : A',
        'C : A',
        'D : B C',
        'E : D',
        'F : D',
        # а теперь другая ветка наследования
        'X',
        'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
        'Z : X',
        'V : Z Y',
        'W : V',
        '8',
        'A G',  # Yes   # A предок G через B/C, D, F
        'A Z',  # No    # Y потомок A, но не Y
        'A W',  # Yes   # A предок W через Y, V
        'X W',  # Yes   # X предок W через Y, V
        'X QWE',  # No    # нет такого класса QWE
        'A X',  # No    # классы есть, но они нет родства :)
        'X X',  # Yes   # родитель он же потомок
        '1 1',  # No    # несуществующий класс
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

    @patch('builtins.input', MagicMock(side_effect=test_input_for_test_inheritance_3))
    def test_inheritance_3(self):
        expected = [
            "Yes"
        ]
        inheritance_proj.enterInputValues()
        actual = inheritance_proj.search_parents_of_classes()
        self.assertListEqual(expected, actual)

    @patch('builtins.input', MagicMock(side_effect=test_input_for_test_inheritance_4))
    def test_inheritance_4(self):
        expected = [
            "Yes",
            "No",
            "Yes",
            "Yes",
            "No",
            "No",
            "Yes",
            "No"
        ]
        inheritance_proj.enterInputValues()
        actual = inheritance_proj.search_parents_of_classes()
        self.assertListEqual(expected, actual)
