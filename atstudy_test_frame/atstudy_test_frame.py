# #-*- coding:utf-8 -*-
# #author:胡久龙
#
# # 实现atstudy测试框架界面及驱动
#

# filedialog：文件对话框
import wx

class UI_testframe():
    def __init__(self):
        self.app=wx.App()
        self.win=wx.Frame(None,title="测试框架1.0",size=(400,500))
        self.panl=wx.Panel(self.win)
        # 定义窗体上的文字
        self.lab_file=wx.StaticText(self.panl,label='测试框架配置文件')
        # 定义文件输入框
        self.txt_file=wx.TextCtrl(self.panl)
        # 定义文件打开按钮
        self.but_open=wx.Button(self.panl,label='打开')
        # 执行按钮
        self.but_run=wx.Button(self.panl,label='执行')
        # 重置按钮
        self.but_rest = wx.Button(self.panl, label='重置')
        # 退出按钮
        self.but_exit = wx.Button(self.panl, label='退出')

    def UI_layout(self):

        # 定义水平放置的  flag=wx.ALL代表默认的上下左右设置
        self.box=wx.BoxSizer()
        # 将对应的控件加入到box中,proportion=1,border=10,flag=wx.RIGHT|wx.BOTTOM|wx.EXPAND|wx.Top
        self.box.Add(self.lab_file,flag=wx.ALL,border=10)
        self.box.Add(self.txt_file,flag=wx.ALL,border=10)
        self.box.Add(self.but_open,flag=wx.ALL,border=10)

        #添加其他控件
        self.box1=wx.BoxSizer()
        self.box1.Add(self.but_run,flag=wx.ALL,border=10)
        self.box1.Add(self.but_rest,flag=wx.ALL,border=10)
        self.box1.Add(self.but_exit,flag=wx.ALL,border=10)

        # 定义垂直按钮  flag=wx.TOP代表与上面的间距
        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box2.Add(self.box,flag=wx.TOP,border=20)
        self.box2.Add(self.box1)
        self.panl.SetSizer(self.box2)

    def run(self):
        self.win.Show(True)
        self.app.MainLoop()
if __name__ == '__main__':
    obj=UI_testframe()
    obj.UI_layout()
    obj.run()