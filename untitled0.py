import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#app_setup
app=Tk()
app.title("BMI CALCULATOR")
app.geometry("470x580+300+200")
app.config(bg="#723c70")
app.resizable(False,False)

#backend
def BMI():
    try:
        h=float(height_entry.get())
        w=float(weight_entry.get())
        if var2.get()=="ft":
            h *= 30.48
        if var1.get()=="lbs":
            w *= 0.453592
        bmi=w/((h/100)**2)
        bmi=int(bmi)
        x.config(text=bmi)
        if bmi<18.5:
            y.config(text="UNDERWEIGHT")
            z.config(text="Start eating more!!")
        elif bmi>18.5 and bmi<25:
            y.config(text="NORMAL")
            z.config(text="Keep maintaing this Healthy diet!")
        elif bmi>25 and bmi<30:
            y.config(text="OVERWEIGHT")
            z.config(text="Start eating healthy!!")
        else:
            y.config(text="OBESE")
            z.config(text="Start eating healthy!!")
    except ValueError:
        messagebox.showerror("Error","Enter a valid number!")
    except ZeroDivisionError:
        messagebox.showerror("Error","Height cannot be 0!")

#icon


#top 

#bottom_box
Label(app,width="72",height="18",bg="#5c4d7d").pack(side=BOTTOM)


Label(app,bg="#5c4d7d").place(x=20,y=100)
Label(app,bg="#5c4d7d").place(x=240,y=100)

#fonts
font2=("Times",20,"bold italic underline")
font3=("Arial",30,"bold")
font1=("Arial",18,"bold")

#Text_files
height_label=tkinter.Label(app,font=font2,text="HEIGHT",fg="#ffffff",bg="#5c4d7d",justify=CENTER)
height_label.place(x=75,y=120)
weight_label=tkinter.Label(app,font=font2,text="WEIGHT",fg="#ffffff",bg="#5c4d7d",justify=CENTER)
weight_label.place(x=290,y=120)

#entry_boxes
Height=StringVar()
Weight=StringVar()
height_entry=Entry(app,font=font3,width=8,justify=CENTER)
height_entry.place(x=35,y=170)
weight_entry=Entry(app,font=font3,width=8,justify=CENTER)
weight_entry.place(x=255,y=170)

#drop-down_list
var1=StringVar()
var2=StringVar()
var1.set("PARAMETERS")
var2.set("PARAMETERS")
weight_opt=["Kg","lbs"]
height_opt=["cm","ft"]
height_opt=OptionMenu(app,var2,*height_opt)
height_opt.place(x=70,y=230)
weight_opt=OptionMenu(app,var1,*weight_opt)
weight_opt.place(x=290,y=230)

#Button
but=Button(app,text="CALCULATE BMI",width=15,height=2,command=BMI)
but=but.place(x=180,y=330)

#result_display
x=Label(app,font="Times 40 bold",bg="#5c4d7d")
x.place(x=160,y=405)
bmi_text=tkinter.Label(app,font='Times 40 bold',text="BMI=",bg="#5c4d7d",justify=CENTER)
bmi_text.place(x=20,y=405)

y=Label(app,font="Times 25 bold",bg="#5c4d7d")
y.place(x=175,y=460)
result_text=tkinter.Label(app,font='Times 25 bold',text="RESULT=",bg="#5c4d7d",justify=CENTER)
result_text.place(x=20,y=460)

z=Label(app,font="Times 16 bold",bg="#5c4d7d")
z.place(x=120,y=500)
status_txt=tkinter.Label(app,font='Times 16 bold',text="STATUS=",bg="#5c4d7d",justify=CENTER)
status_txt.place(x=20,y=500)

app.mainloop()