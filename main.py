# -*- coding: UTF-8 -*-
import time
import datetime
import os
import hashlib

import wx
import xlrd
from docxtpl import DocxTemplate
import wx._adv, wx._html

import noname

class MianWindow(noname.MyFrame1):
    def __init__(self, master):
        super(MianWindow, self).__init__(master)
        self.temp_dath = None
        self.data_dath = None
        self.dir_dath = None
        self.desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        self.tempPicker.SetInitialDirectory(self.desktop)
        self.dataPicker.SetInitialDirectory(self.desktop)
        self.dirPicker.SetInitialDirectory(self.desktop)
        self.textShow.WriteText('Welcome to the batch Template software.'+'\n\n')
        self.date1 = time.strftime('%Y-%m-%d', time.localtime())
        self.time1 = time.strftime('%H-%M-%S', time.localtime())
        self.expired = self.loadDate()
        self.textShow.WriteText('Data: '+self.date1+'\n')
        self.textShow.WriteText('Time: '+self.time1+'\n\n')
        self.textShow.WriteText('The software will expire on '+self.expired+'\n\n')
        self.textShow.WriteText('')

    def loadDate(self):
        return '2019-04-30'

    def openTempFile(self, event):
        if self.date1 > self.expired:
            self.textShow.WriteText('The software has expired.\n')
            return
        self.temp_dath = self.tempPicker.GetPath()
        print('Trmplate File:', self.temp_dath)
        self.textShow.WriteText('Trmplate File:'+self.temp_dath+"\n")
        event.Skip()
            
    def openDataFile(self, event):
        if self.date1 > self.expired:
            self.textShow.WriteText('The software has expired.\n')
            return
        self.data_dath = self.dataPicker.GetPath()
        print('Data File:', self.data_dath)
        self.textShow.WriteText('Data File:'+self.data_dath+"\n")
        wookbook = xlrd.open_workbook(self.data_dath)
        sheet01 = wookbook.sheet_by_index(0)
        self.temp_list = []
        if sheet01.nrows > 1:
            tt = [i.value for i in sheet01.row(0)]
            for i in range(1, sheet01.nrows):
                td = [i.value for i in sheet01.row(i)]
                self.temp_list.append({k:v for k,v in zip(tt, td)})
        event.Skip()
    
    def openDataDir(self, event):
        if self.date1 > self.expired:
            self.textShow.WriteText('The software has expired.\n')
            return

        self.dir_dath = self.dirPicker.GetPath()
        self.textShow.WriteText('Saved Dir:'+self.dir_dath+"\n")
        print('Saved Dir:', self.dir_dath)
        event.Skip()
    
    def startButtonFunc( self, event ):
        if self.date1 > self.expired:
            self.textShow.WriteText('The software has expired.\n')
            return
        if self.temp_dath == None or len(self.temp_dath) == 0:
            self.textShow.WriteText('Please choice a template file.\n')
            return
        if self.data_dath == None or len(self.data_dath) == 0:
            self.textShow.WriteText('Please choice a data file.\n')
            return
        if self.dir_dath == None or len(self.dir_dath) == 0:
            self.textShow.WriteText('Please choice a destination folder.\n')
            return

        print(f'Batch Deal Start: Total {len(self.temp_list)}')
        listlen = len(self.temp_list)
        for i in range(100):
            if i < listlen:
                v = (i+1)*100/listlen
                v = v if 0 <= v <= 100 else 100
                self.gauge.SetValue(v) 
                self.doc = DocxTemplate(self.temp_dath)
                dtmp = self.temp_list[i]
                tname = str([i for i in dtmp.values()][0]) +'.docx'
                self.doc.render(dtmp)
                name = os.path.join(self.dir_dath, tname)
                print('Create File:', name)
                self.textShow.WriteText('Create File:'+name+"\n"); 
                self.doc.save(name)
        print('Batch Deal End')

if __name__ == '__main__':
    app = wx.App()
    win = MianWindow(None)
    win.Show()
    app.MainLoop()
