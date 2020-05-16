from tkinter import *
root = Tk()
root.title('My First GUI...')
root.geometry('500x300')
root.configure(bg='red')
lab1 = Label(root,text='Hello World',width=20,height=2,anchor=N,bg='blue',fg='white',
             font=('chiller',35,'italic bold underline'),cursor='watch',relief=RIDGE,bd=5,
             )
lab1.pack()
root.mainloop()