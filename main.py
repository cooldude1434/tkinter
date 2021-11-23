from tkinter import *


window = Tk()


window.title("First GUI")
window.minsize(width=500,height=300)
window.config(padx=200,pady=200)


#label - its one of the component

my_label = Label(text="I am label",font=("Arial",24,"bold"))
my_label.grid(column=10,row=10)  #to show the componenets in window
my_label.config(padx=20,pady=10)
my_label["text"] = "New label"

def button_clicked():
    my_label.config(text=f"{input.get()}")

#butto



button = Button(text="click me",command =button_clicked)
button.grid(column=40,row=10)



button = Button(text="click me button 2",command =button_clicked)
button.grid(column=20,row=20)

#entry componenet

input = Entry(width=20)
input.grid(column=50,row=30)
input.get()







window.mainloop()

