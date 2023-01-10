from tkinter import *
from datetime import *
my_var=Tk() #object for tkinter
my_var.geometry("820x600") 
my_var.title("Project-1")  
my_var.configure(bg="yellow")
birth_year = StringVar()
birth_month = StringVar()
birth_date = StringVar()
Label(my_var,text="age calculator",font="arial 25 bold",bg="yellow",fg="blue").pack()
Label(my_var,text="Year of birth",font="arial 20 bold",bg="yellow",fg="black").place(x=40,y=100)
x1=Entry(my_var,textvariable=birth_year,font="arial 15 bold",width="30")
x1.place(x=260,y=105)
Label(my_var,text="Month of birth",font="arial 20 bold",bg="yellow",fg="black").place(x=40,y=200)
x2=Entry(my_var,textvariable=birth_month,font="arial 15 bold",width="30")
x2.place(x=260,y=200)
Label(my_var,text="date of birth",font="arial 20 bold",bg="yellow",fg="black").place(x=40,y=300)
x3=Entry(my_var,textvariable=birth_date,font="arial 15 bold",width="30")
x3.place(x=260,y=300)
def dummy():
    r1=int(birth_year.get())
    r2=int(birth_month.get())
    r3=int(birth_date.get())
    r=date.today()
    rf= date(r1,r2,r3)
    days=str(r-rf)
    age=0
    len1 = len(days)
    str1 = days[:len1-14]
    days1 = int(str1)
    year1=r.year
    for i in range(r1+1,year1):
        if ((i%400==0) or (i%100!=0) and (i%4==0)):
            days1-=366
            age+=1
        else:
            days1-=365
            age+=1
    if(days1>=365):
        age+=1
    Label(my_var,text="Here's your age : ",font="arial 20 bold",bg="yellow",fg="black").place(x=150,y=410)
    Label(my_var,text=str(age),font="arial 17 bold",bg="yellow",fg="black").place(x=400,y=410)
Button(my_var,text="click here for your age",command=dummy,font="arial 12 bold",fg="green").place(x=600,y=500)
my_var.mainloop()


    
    

