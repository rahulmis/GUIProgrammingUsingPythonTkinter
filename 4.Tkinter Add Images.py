from tkinter import *
root = Tk()
root.title('My First GUI...')
root.geometry('500x300')
root.configure(bg='red')
def hello():
    print("Hello ")
im = PhotoImage(file='pause.png')
im = im.subsample(2,2)
btn1 = Button(root,text='click    ',bg='yellow',fg='green',font=('arial',25,'bold'),activebackground='blue',
              width=200,height=100,anchor=N,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=hello,
              image=im,compound=RIGHT)
btn1.pack()

lab1 = Label(root,text='Hello',anchor=N,bg='white',fg='black',
             font=('chiller',35,'italic bold underline'),cursor='watch',relief=RIDGE,bd=5,
             image=im,compound=BOTTOM)
lab1.pack()


root.mainloop()