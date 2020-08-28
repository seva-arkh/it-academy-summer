'''Оформите указанную задачу из прошлых домашних в виде функции и
покройте тестами. Учтите, что в функцию могут быть переданы некорректные
значения, здесь может пригодится ‘assertRaises’. Не нужно переделывать
функцию для того чтобы она ловила все возможные ситуации сама.
'''

import unittest
import ddt

import b65


@ddt.ddt
class TestB65(unittest.TestCase):

    @ddt.data((10,8),(20,16),(1,1),(13,16)(28,4))

    @ddt.unpack
    def test_case(self, num1, num2):
        result = b65.b_5(num1)
        print(num1, b65.b_5(num1), num2)
        self.assertEqual(result, num2)

if __name__ == '__main__':
    unittest.main()
