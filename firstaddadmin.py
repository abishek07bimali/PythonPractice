from tkinter import *
Aces=Tk()


def adminsign():
    top=Toplevel()
    top.geometry('380x350')
    top.title('Forgot Password')

    Frame(top,bg='#b4cef3',height=400,width=400).place(x=0,y=0)
    Label(top, text='RESET PASSWORD', bg="#b4cef3", fg='white', font=('Arial',20,'bold')).place(x=50, y=20)


    mail_ent=Entry(top)
    mail_ent.place(x=40, y=75,width=290, height=30)






Aces.mainloop()