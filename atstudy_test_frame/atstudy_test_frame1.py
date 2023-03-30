# #-*- coding:utf-8 -*-
# #author:胡久龙
#
# # 实现atstudy测试框架界面及驱动
#测试数据

# filedialog：文件对话框
import csv

import wx
import os

class UI_testframe():
    def __init__(self):
        self.app=wx.App()
        self.win=wx.Frame(None,title="测试框架1.0",size=(400,500))
        self.panl=wx.Panel(self.win)
        # 定义窗体上的文字
        self.lab_file=wx.StaticText(self.panl,label='测试框架配置文件')
        # 定义文件输入框  设置为只读文本框：
        self.txt_file=wx.TextCtrl(self.panl,style=wx.TE_READONLY)
        # 定义文件打开按钮
        self.but_open=wx.Button(self.panl,label='打开')
        # 执行按钮
        self.but_run=wx.Button(self.panl,label='执行')
        # 重置按钮
        self.but_rest = wx.Button(self.panl, label='重置')
        # 退出按钮
        self.but_exit = wx.Button(self.panl, label='退出')
        # 定义获取文件路径 初始化为空
        self.configfile=""

    def UI_layout(self):

        # 定义水平放置的  flag=wx.ALL代表默认的上下左右设置
        self.box=wx.BoxSizer()
        # 将对应的控件加入到box中,proportion=1,border=10,flag=wx.RIGHT|wx.BOTTOM|wx.EXPAND|wx.Top
        self.box.Add(self.lab_file,flag=wx.ALL,border=10)
        self.box.Add(self.txt_file,proportion=2,flag=wx.ALL,border=10)


        #添加其他控件
        self.box1=wx.BoxSizer()
        self.box1.Add(self.but_open, flag=wx.ALL, border=10)
        self.box1.Add(self.but_run,flag=wx.ALL,border=10)
        self.box1.Add(self.but_rest,flag=wx.ALL,border=10)
        self.box1.Add(self.but_exit,flag=wx.ALL,border=10)

        # 定义垂直按钮  flag=wx.TOP代表与上面的间距
        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box2.Add(self.box,flag=wx.TOP|wx.EXPAND,border=40)
        self.box2.Add(self.box1)
        self.panl.SetSizer(self.box2)

    # 定义一个事件绑定openfile方法
    def UI_event(self):
        self.but_open.Bind(wx.EVT_BUTTON,self.openfile)
        self.but_run.Bind(wx.EVT_BUTTON,self.rundriver)
        self.but_rest.Bind(wx.EVT_BUTTON, self.clear)
        self.but_exit.Bind(wx.EVT_BUTTON, self.exit)
    # 创建一个openfile方法用来重新打开一个窗口选择文件    FileDialog：文件对话框
    def openfile(self,event):
        self.dlgd_open=wx.FileDialog(self.panl,message='打开文件',wildcard='*.csv',style=wx.FD_OPEN)
        if self.dlgd_open.ShowModal()==wx.ID_OK:
            self.txt_file.AppendText(self.dlgd_open.GetPath())
            # 获取配置文件的名称
            self.configfile=self.dlgd_open.GetPath()

     # 重置方法清空输入框中的值
    def clear(self,event):
        self.txt_file.SetValue('')

    # 关闭窗体
    def exit(self,event):
        self.win.Close()


    # 调用驱动文件的方法
    def rundriver(self,event):
        txtfile=self.txt_file.GetValue()
        if txtfile=='':
            dlg=wx.MessageDialog(None,'必须选择配置文件！','错误提示',wx.YES_DEFAULT|wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
                dlg.Destroy()
            return 0
        objfile=driver_testframe()
        objfile.runtestfile(self.configfile)



    def UI_show(self):
        self.win.Show(True)
        self.app.MainLoop()

# 定义类读取配置文件信息的方法
class driver_testframe():
    def runtestfile(self,configfile):
        file=open(configfile,"r")
        txts=csv.reader(file)
        headre=next(txts)
        for txt in txts:
            strScript=(fr"python {txt[1]}")
            os.system(strScript)



if __name__ == '__main__':
    obj=UI_testframe()
    obj.UI_layout()
    obj.UI_event()
    obj.UI_show()

