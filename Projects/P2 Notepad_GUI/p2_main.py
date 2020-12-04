from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import re
import os
import time

root=Tk()
root.geometry('800x500')
root.title('Notepad')

txt=Text(root,font=('Times New Roman',16), padx=10, pady=5)
txt.pack(expand=True,fill=BOTH)

fileName = ''
last_text = ''

global selected_text
selected_text =""
#------------ Functions of file menu -------------------------------

def new_file(event):
	global last_text
	cursor_pos = txt.index(INSERT)
	if last_text == txt.get('1.0', 'end-1c'):
		txt.delete('1.0', END)
		last_text = ''
	else:
		ask = messagebox.askyesno(title='Notepad',message='Do you want to save this file?')
		if not ask :
			txt.delete('1.0',END)
		else:
			save()
			txt.delete('1.0',END)
	root.title('New File')

def open_file(event):
	txt.delete('1.0', 'end-1c')
	global last_text
	file=filedialog.askopenfilename(title="Open File")
	global fileName
	fileName = file
	fr=open(file,'r')
	root.title(os.path.split(file)[1])
	txt.insert(END,fr.read())
	last_text = txt.get('1.0', 'end-1c')

def save(event):
	global last_text
	last_text = txt.get('1.0', 'end-1c')
	if fileName == '':
		save_as()
	else:
		file1=open(fileName,'w')
		file1.write(txt.get('1.0','end-1c'))
		file1.close()
	# messagebox.showinfo(title="Notepad",message="Your file has been saved successfully")

def save_as():
	global last_text
	last_text = txt.get('1.0', 'end-1c')
	tmp=filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
	global fileName
	fileName = tmp
	file1=open(tmp,'w')
	file1.write(txt.get('1.0','end-1c'))
	file1.close()
	root.title(os.path.split(tmp)[1])
	messagebox.showinfo(title="Notepad",message="Your file has been saved successfully")
	pass

def exit(event):
	global last_text
	if not txt.get('1.0', 'end-1c') == last_text:
		ask_save=messagebox.askyesno(title='Notepad',message='Do you want to save the changes?')
		if ask_save:
			if fileName == '':
				save_as()
			else:
				save()
	root.destroy()

#------------------------Functions of edit menu------------------------------------
def cut_text(event):
	global selected_text
	if event:
		selected_text = root.clipboard_get()
	else:
		if txt.selection_get():
			selected_text = txt.selection_get()
			txt.delete("sel.first","sel.last")
			root.clipboard_clear()
			root.clipboard_append(selected_text)

def copy_text(event):
	global selected_text
	if event:
		selected_text = root.clipboard_get()
	else:
		if txt.selection_get():
			selected_text = txt.selection_get()
			root.clipboard_clear()
			root.clipboard_append(selected_text)

def paste_text(event):
	global selected_text
	if event:
		selected_text = root.clipboard_get()
	else:
		if selected_text:
			cursor_pos = txt.index(INSERT)
			txt.insert(cursor_pos, selected_text)

def find_replace_closed(box_to_close):
	txt.tag_remove('found', '1.0', END)
	box_to_close.destroy()

def find(s1):
	s = s1.get()
	txt.tag_remove('found', '1.0', END)
	if s:
		idx = '1.0'
		while 1:
			idx = txt.search(s, idx, nocase=1, stopindex=END)
			print("searching...")
			if not idx:
				break
			last_idx = '% s+% dc' % (idx, len(s))
			txt.tag_add('found', idx, last_idx)
			idx = last_idx
		txt.tag_config('found', background='cyan')
	pass

def replace(s1,s2):
	s = s1.get()
	r = s2.get()
	txt.tag_remove('found', '1.0', END)
	if s and r:
		idx = '1.0'
		while True:
			idx = txt.search(s, idx, nocase=1, stopindex=END)
			if not idx:
				break
			last_idx = '% s+% dc' % (idx, len(s))
			txt.delete(idx, last_idx)
			txt.insert(idx, r)

			last_idx = '% s+% dc' % (idx, len(r))
			txt.tag_add('found', idx, last_idx)
			idx = last_idx
		txt.tag_config('found', background='cyan')
	pass

def find_window():
	# regex = re.compile
	find_box = Toplevel(root)
	find_box.title("Find & Replace")
	find_box.geometry('250x100')

	s1 = StringVar()
	# l1 =Label(find_box,text="Find :",font=('Arial',14),padx=10).grid(row=0)
	l1 =Label(find_box,text="Find :",font=('Arial',14),padx=10).place(x=-10,y=5,width=100)
	# e1 =Entry(find_box,textvariable=s1).grid(row=0,column=1)
	e1 =Entry(find_box,textvariable=s1).place(x=80,y=10,width=150)
	# b1 = Button(find_box,text='Find',command=find,font=('Arial',13)).grid(row=1,column=1)
	b1 = Button(find_box,text='Find',command=lambda: find(s1),font=('Arial',13)).place(x=70,y=40,width=100)
	find_box.protocol("WM_DELETE_WINDOW", lambda: find_replace_closed(find_box))
	pass

def find_and_replace():
	find_and_replace_box = Toplevel(root)
	find_and_replace_box.title("Find & Replace")
	find_and_replace_box.geometry('300x100')

	s1, s2= StringVar(),StringVar()

	Label(find_and_replace_box,text="Find :",font=('Arial',14),padx=30).grid(row=0)
	Label(find_and_replace_box,text="Replace :",padx=30,font=('Arial',14)).grid(row=1)

	e1 =Entry(find_and_replace_box,textvariable=s1).grid(row=0,column=1)
	e2 =Entry(find_and_replace_box,textvariable=s2).grid(row=1,column=1)

	b1 = Button(find_and_replace_box,text='Find',command=lambda: find(s1),padx=40,font=('Arial',13)).grid(row=2,column=0)
	b2 = Button(find_and_replace_box,text='Replace All',command=lambda: replace(s1, s2),padx=30,font=('Arial',13)).grid(row=2,column=1)
	find_and_replace_box.protocol("WM_DELETE_WINDOW", lambda: find_replace_closed(find_and_replace_box))
	pass

#-------------------------Functions of stats menu-----------------------------------
def word_count():
	count = len(re.findall("\s", txt.get('1.0','end-1c')))
	messagebox.showinfo(title="Notepad",message= f"Word Count = {count}")
	pass

def char_count():
	count = len(re.findall('\w|\W', txt.get('1.0','end-1c'))) - len(re.findall("\s", txt.get('1.0','end-1c')))
	messagebox.showinfo(title="Notepad",message= f"Total characters = {count}")
	pass

def created_time():
	messagebox.showinfo(title="Notepad",message= f"Created Time : {time.ctime(os.path.getctime(fileName))}")
	pass

def modified_time():
	messagebox.showinfo(title="Notepad",message= f"Last Modified : {time.ctime(os.path.getmtime(fileName))}")
	pass

#-----------------------------All Functions Completed--------------------------------
menu_bar = Menu(root)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New   [Ctrl+n]',command=lambda: new_file(0))
file_menu.add_command(label='Open [Ctrl+o]',command=lambda: open_file(0))
file_menu.add_command(label='Save   [Ctrl+s]',command=lambda: save(0))
file_menu.add_command(label='Save as',command=save_as)
file_menu.add_command(label='Exit   [Ctrl+w]',command=lambda: exit(0))
menu_bar.add_cascade(label='File',menu=file_menu)

edit_menu=Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='Cut    	 [Ctrl+x]',command=lambda: cut_text(0))
edit_menu.add_command(label='Copy 	 [Ctrl+c]',command=lambda: copy_text(0))
edit_menu.add_command(label='Paste  [Ctrl+v]',command=lambda: paste_text(0))
edit_menu.add_command(label='Find',command=find_window)
edit_menu.add_command(label='Find & Replace',command=find_and_replace)
menu_bar.add_cascade(label='Edit',menu=edit_menu)

stats_menu=Menu(menu_bar,tearoff=0)
stats_menu.add_command(label='Word Count',command=word_count)
stats_menu.add_command(label='Char Count',command=char_count)
stats_menu.add_command(label='Created Time',command=created_time)
stats_menu.add_command(label='Modified Time',command=modified_time)
menu_bar.add_cascade(label='Stats',menu=stats_menu)

root.config(menu=menu_bar)

root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)
root.bind('<Control-Key-s>',save)
root.bind('<Control-Key-w>', exit)
root.bind('<Control-Key-o>', open_file)
root.bind('<Control-Key-n>', new_file)

root.protocol("WM_DELETE_WINDOW", lambda: exit(0))

root.mainloop()