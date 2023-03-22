#-*- coding:utf-8 -*-
#author:胡久龙
import wx

class UI():
    def __init__(self):
        self.app = wx.App()
        self.win = wx.Frame(None, title="测试框架1.0", size=(400, 500))
        self.panl = wx.Panel(self.win)
        # 定义窗体上的文字
        self.lab_file = wx.StaticText(self.panl, label='测试框架配置文件')
        # 定义文件输入框
        self.txt_file = wx.TextCtrl(self.panl)
        # 定义文件打开按钮
        self.but_open = wx.Button(self.panl, label='打开')
        # 执行按钮
        self.but_run = wx.Button(self.panl, label='执行')
        # 重置按钮
        self.but_rest = wx.Button(self.panl, label='重置')
        # 退出按钮
        self.but_exit = wx.Button(self.panl, label='退出')

        self.dlgd=wx.FileDialog(self.panl,message='打开文件',wildcard='*.csv',style=wx.FD_OPEN)
        if self.dlgd.ShowModal()==wx.ID_OK:
            self.txt_file.AppendText(self.dlgd.GetPath())

if __name__ == '__main__':
    obj=UI()
