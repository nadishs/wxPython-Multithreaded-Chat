#Python program to implement client-server chat using multithreading with GUI using wxPython 
#Client Program

import socket
from threading import Thread
import sys
import wx



app = wx.App()
win = wx.Frame(None, title = "wxChat Client", size = (410, 335))
win.Show()

MessageBox = wx.TextCtrl(win, pos=(5,5), size= (390,260), style = wx.TE_MULTILINE | wx.HSCROLL)
SendBox = wx.TextCtrl(win, pos = (5, 270), size= (200,25))
sumButton = wx.Button(win, label= 'Send', pos = (225,270), size = (80,25))


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))

MessageBox.AppendText("Connection to server established...\n")

def send_to_server(x):
		msg =  SendBox.GetValue()
		s.send(msg)
		MessageBox.AppendText("You: " + msg+ '\n')


def get_from_server():
	while 1:
		msg = s.recv(100)
		if msg == 'exit':
			quit()
			sys.exit()
			break
		else:
			MessageBox.AppendText("Server: " + msg + '\n')

sumButton.Bind(wx.EVT_BUTTON, send_to_server)

while True:
	try:
		t2 = Thread(target = get_from_server)
		t3= Thread(target = app.MainLoop)
		t2.start()
		t3.start()
	except:
		pass
s.close()

