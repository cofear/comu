# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Template File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tempPicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Choice Template File", u"*.docx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer1.Add( self.tempPicker, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.myPhoto = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,200 ), 0 )
		gbSizer1.Add( self.myPhoto, wx.GBPosition( 0, 4 ), wx.GBSpan( 4, 4 ), wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Data File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textShow = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL|wx.WANTS_CHARS )
		self.textShow.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gbSizer1.Add( self.textShow, wx.GBPosition( 4, 0 ), wx.GBSpan( 7, 10 ), wx.ALL|wx.EXPAND, 5 )
		
		self.dataPicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Choice Data File", u"*.xlsx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer1.Add( self.dataPicker, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Saved Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Choice Saved Path", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer1.Add( self.dirPicker, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gbSizer1.Add( self.m_staticText8, wx.GBPosition( 12, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.gauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge.SetValue( 0 ) 
		self.gauge.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gauge.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gbSizer1.Add( self.gauge, wx.GBPosition( 12, 1 ), wx.GBSpan( 1, 9 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.startButton = wx.Button( self, wx.ID_ANY, u"Beach Deal Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.startButton, wx.GBPosition( 14, 5 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.tempPicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.openTempFile )
		self.dataPicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.openDataFile )
		self.dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.openDataDir )
		self.startButton.Bind( wx.EVT_BUTTON, self.startButtonFunc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def openTempFile( self, event ):
		event.Skip()
	
	def openDataFile( self, event ):
		event.Skip()
	
	def openDataDir( self, event ):
		event.Skip()
	
	def startButtonFunc( self, event ):
		event.Skip()
	

