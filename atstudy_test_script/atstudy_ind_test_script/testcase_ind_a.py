#-*- coding:utf-8 -*-
#author:胡久龙

class testcase_ind_a():
    def __init__(self):
        print('testcase_ind_a初始化方法')
    def test_case1(self):
        print('testcase_ind_a测试用例方法1')
    def test_case2(self):
        print('testcase_ind_a测试用例方法2')

if __name__ == '__main__':
    obj=testcase_ind_a()
    obj.test_case1()
    obj.test_case2()