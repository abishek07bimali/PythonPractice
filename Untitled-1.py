from tkinter import *
window=Tk()
window.geometry("480x350")
w=Label(window,text="calculator",fg="green")
w.grid(row=0,column=2)

A=Entry(window,width=55,borderwidth=5)
A.grid(row=2,column=0,columnspan=3 ,padx=10,pady=10)

B=Button(window,text="1",fg="brown",padx=40,pady=20)
B.grid(row=5,column=0)

C=Button(window,text="2",fg="brown",padx=40,pady=20)
C.grid(row=5,column=1)

D=Button(window,text="3",fg="brown",padx=40,pady=20)
D.grid(row=5,column=2)

E=Button(window,text="4",fg="brown",padx=40,pady=20)
E.grid(row=6,column=0)

f=Button(window,text="5",fg="brown",padx=40,pady=20)
f.grid(row=6,column=1)

g=Button(window,text="6",fg="brown",padx=40,pady=20)
g.grid(row=6,column=2)

H=Button(window,text="7",fg="brown",padx=40,pady=20)
H.grid(row=7,column=0)

i=Button(window,text="8",fg="brown",padx=40,pady=20)
i.grid(row=7,column=1)

j=Button(window,text="9",fg="brown",padx=40,pady=20)
j.grid(row=7,column=2)

k=Button(window,text="0",fg="brown",padx=40,pady=20)
k.grid(row=8,column=1)

l=Button(window,text="=",fg="brown",padx=40,pady=20)
l.grid(row=8,column=2)

m=Button(window,text="Clear",fg="brown",padx=40,pady=20)
m.grid(row=8,column=0)

N=Button(window,text="+",fg="brown",padx=40,pady=20)
N.grid(row=5,column=3)

o=Button(window,text="-",fg="brown",padx=40,pady=20)
o.grid(row=6,column=3)
p=Button(window,text="/",fg="brown",padx=40,pady=20)
p.grid(row=7,column=3)

q=Button(window,text="x",fg="brown",padx=40,pady=20)
q.grid(row=8,column=3)


window.mainloop()