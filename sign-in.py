from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Login")
window.config(bg="#f1faee")

lbl1=Label(window,text="Sign in",font=("",40),fg="#457b9d",bg="#f1faee")
lbl1.pack(anchor="center")


lbl2=Label(window,text="Email:",font=("",30),fg="#457b9d",bg="#f1faee")
lbl2.place(x=10,y=90)

ent1=Entry(window)
ent1.place(x=200,y=100)



lbl3=Label(window,text="Password:",font=("",30),fg="#457b9d",bg="#f1faee")
lbl3.place(x=10,y=170)

ent3=Entry(window)
ent3.place(x=200,y=180)

def save():
    f = open("Save.txt", "r")
    if ent3.get() == f.read():
        messagebox.showinfo("Signed in","Signed in")
    else:
        messagebox.showerror("Your pass or email is wrong","Your pass or email is wrong")



btn1=Button(window,text="Apply",font=("",25),bg="#f1faee",fg="#457b9d",command=save)
btn1.place(x=150,y=300)
window.mainloop()