# Student Login System -------------------------------------------
from tkinter import*
from tkinter import messagebox

def login():
    name=entry1.get()
    roll=entry2.get()
    registration=entry3.get()
    department=entry4.get()

    if (name=="" and roll=="" and department==""):
        messagebox.showinfo("","Blank Not Allow")

    if(name=="Abid Hasan"):
        messagebox.showinfo("","Name Was Submit")
    else:
        messagebox.showinfo("","Please Enter The Correct Name")
    if(roll=="683800"):
        messagebox.showinfo("","Roll Was submit")
    else:
         messagebox.showinfo("","Please Enter The Correct Roll")
    if(registration=="1502227892"):
        messagebox.showinfo("","Registration Was submit")
    else:
        messagebox.showinfo("","Please Enter The Correct Registration")
    if(department=="TCT"):
        messagebox.showinfo("","Department Was submit")
    else:
        messagebox.showinfo("","Please Enter The Correct Department")
    if (name=="Abid Hasan" and roll=="683800" and registration=="1502227892" and department=="TCT"):
        messagebox.showinfo("","Name : Abid Hasan, Roll : 683800, Registration : 1502227892, CGPA : 3.71")
    else:
        messagebox.showinfo("","Did Not Find Any Information")
    
root=Tk()
root.title("Login")
#root.geometry("300*200")

global entry1
global entry2
global entry3

Label(root,text="Name : ",fg="blue",font=("",20,"bold")).place(x=120,y=30)
Label(root,text="Roll : ",fg="blue",font=("",20,"bold")).place(x=120,y=105)
Label(root,text="Registration : ",fg="blue",font=("",20,"bold")).place(x=120,y=175)
Label(root,text="Department : ",fg="blue",font=("",20,"bold")).place(x=120,y=235)

entry1=Entry(root,bd=5,width=15,font=("",20,"bold"))
entry1.place(x=330,y=30)

entry2=Entry(root,bd=5,width=15,font=("",20,"bold"))
entry2.place(x=330,y=100)

entry3=Entry(root,bd=5,width=15,font=("",20,"bold"))
entry3.place(x=330,y=170)

entry4=Entry(root,bd=5,width=15,font=("",20,"bold"))
entry4.place(x=330,y=230)

Button(root,text="Submit",command=login,height=1,width=11,fg="red",bg="white",bd=6,font=("",17,"bold")).place(x=360,y=300)


root.mainloop()