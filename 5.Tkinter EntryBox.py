from tkinter import *
root = Tk()
root.title('My First GUI...')
root.geometry('500x300')
root.configure(bg='white')
def ff():
    et1.insert(0,'rahu8l')
    print(ss.get())
    # ss.set('')

ss = StringVar()
et1 =Entry(root,bg='yellow',bd=3,fg='green',font=('arial',20,'bold'),insertbackground='green'
           ,insertwidth=5,justify='center',relief=RIDGE,selectbackground='red',selectforeground='blue',
           textvariable=ss)
et1.pack()
et1.focus_set()
bt1 = Button(root,text='click',command=ff)
bt1.pack()
root.mainloop()