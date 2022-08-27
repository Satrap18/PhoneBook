from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import time

def About():
	messagebox.showinfo('About','Phone Book\nAuthor : Satrap18\nVersion : 1.0')



def Home():
	def add():
		con = sqlite3.connect('Phone_Book.db')
		cur = con.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Book(Name TEXT,Phone INTEGER)')
		data = [("" + e1.get(),e2.get())]
		cur.executemany('INSERT INTO Book VALUES(?,?)',data)
		con.commit()
		con.close()
		messagebox.showinfo('Phone Book','Add Successfully')
		e1.delete(0,END)
		e2.delete(0,END)


	def Show():
		window.resizable(True,True)
		con = sqlite3.connect('Phone_Book.db')
		cur = con.cursor()
		cur = cur.execute("SELECT Name FROM Book")
		text = cur.fetchall()
		label1 = Label(window,text=text) 
		label1.pack()

		
	
	window = Tk()
	window.title('Phone Book')
	window.geometry('300x300')
	window.resizable(False,False)

	icon = PhotoImage(file='icons8-call-list-96.png')
	window.iconphoto(True,icon)

	Photo = PhotoImage(file='icons8-male-user-96.png')

	lbl1 = Label(window,image=Photo)
	lbl1.pack()

	lbl2 = Label(window,text='Name and Lastname',font=('arial',15))
	lbl2.pack()

	e1 = Entry(window,font=('arial',15))
	e1.pack()

	lbl3 = Label(window,text='Phone Number',font=('arial',15))
	lbl3.pack()

	e2 = Entry(window,font=('arial',15))
	e2.pack()


	btn = Button(window,text='Add',font=('arial',15),command=add)
	btn.pack(pady=20)

	menubar = Menu(window)

	filemenu = Menu(menubar,tearoff=0)
	filemenu1 = Menu(menubar,tearoff=0)


	menubar.add_cascade(label="Book",menu=filemenu)
	menubar.add_cascade(label="Help",menu=filemenu1)

	filemenu.add_command(label='Show',command=Show)
	filemenu.add_command(label='Update')
	filemenu.add_command(label='Delete')
	filemenu.add_command(label='Exit',command=exit)
	filemenu1.add_command(label='About',command=About)


	window.config(menu=menubar)

	window.mainloop()


Home()