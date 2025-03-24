#Import Section is here
from cProfile import label
from tkinter import *
from time import *

#Functions in here
def update():

    time_string = strftime("%I:%M:%S %p")
    Time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d  %B  %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

# window configration
window = Tk()
window.title("Digital Clock")

#Code in here

Time_label = Label(window,font=("poppins",35),fg="#00FF00",bg="black")
Time_label.pack()

day_label = Label(window,font=("poppins",15),
                  fg="black",
                  bg="white",
                  borderwidth=5,
                  )
day_label.pack()

date_label = Label(window,
                   font=("poppins",10),
                   fg="white",
                   bg="black",
                   )
date_label.pack()

update()
#Window Mainloop
window.mainloop()