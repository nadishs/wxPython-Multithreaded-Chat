#Python program to implement client-server chat using multithreading with GUI using wxPython 
#Server Program


import socket
from threading import Thread
import sys
import wx


app = wx.App()
win = wx.Frame(None, title = "wxChat Server", size = (410, 335))
win.Show()
MessageBox = wx.TextCtrl(win, pos=(5,5), size= (390,260), style = wx.TE_MULTILINE | wx.HSCROLL)
SendBox = wx.TextCtrl(win, pos = (5, 270), size= (200,25))
sumButton = wx.Button(win, label= 'Send', pos = (225,270), size = (80,25))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen(10)
(clientsocket,address) = s.accept()
MessageBox.AppendText("Connection to client established...\n")

def send_to_server(x):
		msg =  SendBox.GetValue()
		
		clientsocket.send(msg)
		MessageBox.AppendText("You: " + msg+ '\n')
		if msg == 'exit':
			quit()
			sys.exit()

def get_from_server():
	while 1:
		msg = clientsocket.recv(100)
		MessageBox.AppendText("Server: " + msg+ '\n')


sumButton.Bind(wx.EVT_BUTTON, send_to_server)

while True:
	try:
		t2 = Thread(target = get_from_server)
		t3= Thread(target = app.MainLoop)
		t2.start()
		t3.start()
	except:
		pass

clientsocket.close()
s.close()

