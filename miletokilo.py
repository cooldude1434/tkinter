from tkinter import *


window = Tk()


window.title("Mile to Km Convertor")
# window.minsize(width=20,height=20)
window.config(padx=20,pady=20)

#create input widget to get miles

input = Entry(width=5,text="0")
input.grid(column=1,row=0)
input.insert(END, string="0")
#

#create labels to print

miles_label = Label(text="Miles",font=("Arial",10,"bold"))
miles_label.grid(column=2,row=0)

isequal_label = Label(text="Is equal to",font=("Arial",10,"bold"))
isequal_label.grid(column=0,row=1)

km_label = Label(text="Km",font=("Arial",10,"bold"))
km_label.grid(column=2,row=1)

def button_clicked():
    # km = round(float(miles) * 1.609, 2)
    miles = float(input.get())
    km = miles * 1.60934

    result_label = Label(text=f"{round(km,2)}",font=("Arial",10,"bold"))
    result_label.grid(column=1,row=1)

#create button
button = Button(text="calcuate",command =button_clicked)
button.grid(column=1,row=3)


window.mainloop()