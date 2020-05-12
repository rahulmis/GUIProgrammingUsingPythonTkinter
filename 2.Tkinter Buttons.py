from tkinter import *
root = Tk()
root.title('My First GUI...')
root.geometry('500x300')
root.configure(bg='red')
def hello():
    print("Hello ")
btn1 = Button(root,text='click',bg='yellow',fg='green',font=('arial',25,'bold'),activebackground='blue',
              width=10,height=2,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=hello)
btn1.pack()


root.mainloop()