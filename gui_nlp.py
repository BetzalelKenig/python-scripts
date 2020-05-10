from tkinter import *
from tkinter import ttk

def click():
	entered_url = textentry.get()

root = Tk()
root.title('Avratech NLP')
root.configure(background='black')


icon = PhotoImage(file='')
#Label(root, image=icon, bg='black').grid(row=0, column=0, sticky=E)

Label(root, text='URL', bg='white', fg='red', font='none 12 bold').pack()


textentry = Entry(root, width=20, bg='white').pack()

run = ttk.Button(root, text='Run', width=6, command=click).pack()


root.mainloop()