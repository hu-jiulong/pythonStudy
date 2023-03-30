#-*- coding:utf-8 -*-
#author:胡久龙



class testcase_ind_c():
    def __init__(self):
        print('这是testcase_ind_c的初始方法')
    def test_case1(self):
        print('这是testcase_ind_c的测试方法1')

    # 创建一个main方法在test1.py测试文件中调用
    def main(self):
        self.test_case1()


if __name__ == '__main__':
    obj=testcase_ind_c()
    obj.test_case1()
