from tkinter import *
root = Tk()
root.geometry('800x400')
# bt1 = Button(root,text='click',width=10,height=2,bg='red')
# bt1.grid(row=0,column=0)
#
# bt1 = Button(root,text='click',width=10,height=2,bg='red')
# bt1.grid(row=0,column=1)
#
# bt1 = Button(root,text='click',width=10,height=2,bg='red')
# bt1.grid(row=0,column=2)
#
# bt1 = Button(root,text='click',width=10,height=2,bg='red')
# bt1.grid(row=0,column=3)
#
# bt1 = Button(root,text='click',width=20,height=2,bg='red')
# bt1.grid(row=1,column=2,columnspan=2)
#
# bt1 = Button(root,text='click',width=20,height=2,bg='red')
# bt1.grid(row=2,column=2,columnspan=2)
#
# bt1 = Button(root,text='click',width=20,height=2,bg='red')
# bt1.grid(row=3,column=2,columnspan=2)
#
#
# bt1 = Button(root,text='click',width=10,height=6,bg='red')
# bt1.grid(row=1,column=0,rowspan=3)
bt1 = Button(root,text='click',width=10,height=5,bg='red')
bt1.grid(row=0,column=0)

bt1 = Button(root,text='click',width=5,height=2,bg='red')
bt1.grid(row=0,column=1,sticky=N)

bt1 = Button(root,text='click',width=50,height=2,bg='red')
bt1.grid(row=1,column=1)


root.mainloop()