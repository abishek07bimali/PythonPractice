from tkinter import *
window=Tk()
window.geometry("400x300")
H=Label(window,text="Registration form",fg="green")
H.place(x=150,y=20)


text=Label(window,text="First name",fg="brown")
text1=Entry(window).place(x=200,y=50)
text.place(x=100,y=50)

D=Label(window,text="Last name",fg="brown")
text1=Entry(window).place(x=200,y=90)
D.place(x=100,y=90)


A=Label(window,text="Email",fg="brown")
text1=Entry(window).place(x=200,y=120)
A.place(x=100,y=120)

E=Label(window,text="Password",fg="brown")
text1=Entry(window,show="*").place(x=200,y=150)
E.place(x=100,y=150)

F=Label(window,text="Confirm Password",fg="brown")
text1=Entry(window,show="*").place(x=200,y=180)
F.place(x=100,y=180)


B=Button(window,text="login",fg="brown")
B.place(x=150,y=240)

C=Button(window,text="Cancel",fg="brown")
C.place(x=200,y=240)




window.mainloop()