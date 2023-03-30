#-*- coding:utf-8 -*-
#author:胡久龙
import wx
import csv
#
# class UI():
#     def __init__(self):
#         self.app = wx.App()
#         self.win = wx.Frame(None, title="测试框架1.0", size=(400, 500))
#         self.panl = wx.Panel(self.win)
#         # 定义窗体上的文字
#         self.lab_file = wx.StaticText(self.panl, label='测试框架配置文件')
#         # 定义文件输入框
#         self.txt_file = wx.TextCtrl(self.panl)
#         # 定义文件打开按钮
#         self.but_open = wx.Button(self.panl, label='打开')
#         # 执行按钮
#         self.but_run = wx.Button(self.panl, label='执行')
#         # 重置按钮
#         self.but_rest = wx.Button(self.panl, label='重置')
#         # 退出按钮
#         self.but_exit = wx.Button(self.panl, label='退出')
#
#         self.dlgd=wx.FileDialog(self.panl,message='打开文件',wildcard='*.csv',style=wx.FD_OPEN)
#         if self.dlgd.ShowModal()==wx.ID_OK:
#             self.txt_file.AppendText(self.dlgd.GetPath())
#
#
# if __name__ == '__main__':
#     obj=UI()


# //////实验

# #-*- coding:utf-8 -*-
# #author:胡久龙
#
# # 实现atstudy测试框架界面及驱动
#

# # filedialog：文件对话框




# import wx
#
# class UI_testframe():
#     def __init__(self):
#         self.app=wx.App()
#         self.win=wx.Frame(None,title="测试框架1.0",size=(400,500))
#         self.panl=wx.Panel(self.win)
#         # 定义窗体上的文字
#         self.lab_file=wx.StaticText(self.panl,label='测试框架配置文件')
#         # 定义文件输入框
#         self.txt_file=wx.TextCtrl(self.panl)
#         # 定义文件打开按钮
#         self.but_open=wx.Button(self.panl,label='打开')
#         # 执行按钮
#         self.but_run=wx.Button(self.panl,label='执行')
#         # 重置按钮
#         self.but_rest = wx.Button(self.panl, label='重置')
#         # 退出按钮
#         self.but_exit = wx.Button(self.panl, label='退出')
#         # 定义获取文件路径
#         self.configfile=''
#
#     def UI_layout(self):
#
#         # 定义水平放置的  flag=wx.ALL代表默认的上下左右设置
#         self.box=wx.BoxSizer()
#         # 将对应的控件加入到box中,proportion=1,border=10,flag=wx.RIGHT|wx.BOTTOM|wx.EXPAND|wx.Top
#         self.box.Add(self.lab_file,flag=wx.ALL,border=10)
#         self.box.Add(self.txt_file,proportion=2,flag=wx.ALL,border=10)
#
#
#         #添加其他控件
#         self.box1=wx.BoxSizer()
#         self.box1.Add(self.but_open, flag=wx.ALL, border=10)
#         self.box1.Add(self.but_run,flag=wx.ALL,border=10)
#         self.box1.Add(self.but_rest,flag=wx.ALL,border=10)
#         self.box1.Add(self.but_exit,flag=wx.ALL,border=10)
#
#         # 定义垂直按钮  flag=wx.TOP代表与上面的间距
#         self.box2 = wx.BoxSizer(wx.VERTICAL)
#         self.box2.Add(self.box,flag=wx.TOP|wx.EXPAND,border=40)
#         self.box2.Add(self.box1)
#         self.panl.SetSizer(self.box2)
#
#     # 定义一个事件绑定openfile方法
#     def UI_event(self):
#         self.but_open.Bind(wx.EVT_BUTTON,self.openfile)
#         self.but_run.Bind(wx.EVT_BUTTON, self.readfile)
#
#     # 创建一个openfile方法用来重新打开一个窗口选择文件    FileDialog：文件对话框
#     def openfile(self,event):
#         self.dlgd_open=wx.FileDialog(self.panl,message='打开文件',wildcard='*.csv',style=wx.FD_OPEN)
#         if self.dlgd_open.ShowModal()==wx.ID_OK:
#             self.txt_file.AppendText(self.dlgd_open.GetPath())
#
#             #对读取文件的路径赋值
#             self.configfile=self.dlgd_open.GetPath()
#
#
#         # 实验读取csv文件
#         # file=open(self.dlgd_open.GetPath(),'r')
#         # txts=csv.reader(file)
#         # for txt in txts:
#         #     print(txt)
#
#     def readfile(self,event):
#         file = open(self.configfile, 'r')
#         txts = csv.reader(file)
#         for txt in txts:
#             print(txt)
#
#     def UI_show(self):
#         self.win.Show(True)
#         self.app.MainLoop()
# if __name__ == '__main__':
#     obj=UI_testframe()
#     obj.UI_layout()
#     obj.UI_event()
#     obj.UI_show()

# 方法一：通过python调用方式执行脚本文件 绝对路径
import os

# strScript=(r"python D:\PycharmProjects\atstudy_testframe\atstudy_test_script\atstudy_ind_test_script\testcase_ind_a.py")
# os.system(strScript)



# 相对路径调用
# strScript=(r"python ..\atstudy_test_script\atstudy_ind_test_script\testcase_ind_a.py")
# os.system(strScript)

# #方法二: 调用main方法进行运行脚本
# from atstudy_test_script.atstudy_ind_test_script.testcase_ind_c import testcase_ind_c
#
# # 定义对象
# obj=testcase_ind_c()
# # 调取main函数
# obj.main()

# 方法三使用unittest框架自带的discover进行脚本执行
import unittest
fdir=r"D:\PycharmProjects\atstudy_testframe\atstudy_test_script\atstudy_ind_test_script"
fname='testcase*'
discover=unittest.defaultTestLoader.discover(fdir,pattern=fname)
runner=unittest.TextTestRunner()
runner.run(discover)









