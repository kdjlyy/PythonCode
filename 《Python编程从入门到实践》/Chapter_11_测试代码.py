# 第十一章 测试代码
import unittest
from name_function import get_formatted_name

# 函数测试
class NameTestCase(unittest.TestCase):
    """测试name_function"""
    def test_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_name2(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest
"""
Ran 2 test in 0.003s

OK
"""
