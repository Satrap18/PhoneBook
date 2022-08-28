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
		con = sqlite3.connect('Phone_Book.db')
		cur = con.cursor()
		cur = cur.execute("SELECT * FROM Book")
		text = cur.fetchall()
		with open('Phone_Book.html', 'w',encoding='utf-8') as file:
			file.write(str(text))
		messagebox.showinfo('Show','You Can See All User in Phone_Book.html')
		
	def delete():
		messagebox.showinfo("Delete","Enter Full Name")
		Toplevel = Tk()
		Toplevel.title('Delete')
		Toplevel.resizable(False,False)
		lbl4 = ttk.Label(Toplevel,text='Delete',font=('arial',15))
		lbl4.pack()
		def delete():
			d = e3.get()
			con = sqlite3.connect('Phone_Book.db')
			cur = con.cursor()
			cur.execute("DELETE FROM Book WHERE name = ?",(d,))
			con.commit()
			Toplevel.destroy()
			messagebox.showinfo("Delete","Delete Successfully")
			con = sqlite3.connect('Phone_Book.db')
			cur = con.cursor()
			cur = cur.execute("SELECT * FROM Book")
			text = cur.fetchall()
			with open('Phone_Book.html', 'w',encoding='utf-8') as file:
				file.write(str(text))
		e3 = Entry(Toplevel,font=('arial',15))
		e3.pack()

		btn = Button(Toplevel,text='Delete',command=delete)
		btn.pack(pady=5)
		Toplevel.mainloop()

		'''
		for t in text:
			pass
		for tt in phone:
			pass
		with open('Phone_Book.html', 'w',encoding='utf-8') as file:
			file.write(str("\n%s\n" % t + ":"))
			file.write(str("\n%s\n" % tt))
		messagebox.showinfo('Show','You Can See All User in Phone_Book.html')
		'''
	def update():
		root = Tk()
		root.title("update")
		root.mainloop()
	window = Tk()
	window.title('Phone Book')
	window.geometry('300x300')
	window.resizable(False,False)

	icon = PhotoImage(file='icons8-call-list-96.png')
	window.iconphoto(True,icon)

	Photo = PhotoImage(file='icons8-male-user-96.png')

	lbl1 = Label(window,image=Photo)
	lbl1.pack()

	lbl2 = Label(window,text='Full Name',font=('arial',15))
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
	filemenu.add_command(label='Update',command=update)
	filemenu.add_command(label='Delete',command=delete)
	filemenu.add_command(label='Exit',command=exit)
	filemenu1.add_command(label='About',command=About)


	window.config(menu=menubar)

	window.mainloop()


Home()