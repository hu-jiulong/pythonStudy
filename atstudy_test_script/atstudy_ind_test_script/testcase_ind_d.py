#-*- coding:utf-8 -*-
#author:胡久龙

import unittest


class testcase_ind_d(unittest.TestCase):
    def setUp(self):
        print('这是testcase_ind_d的setup方法')
    def test_case1(self):
        print('这是testcase_ind_d的case1方法')
    def test_case2(self):
        print('这是testcase_ind_d的case2方法')
    def test_case3(self):
        print('这是testcase_ind_d的case3方法')
    def tearDown(self):
        print('这是testcase_ind_d的tearDown方法')
if __name__ == '__main__':
    unittest.main()
