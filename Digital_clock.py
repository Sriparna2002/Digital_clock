
# import whole modules
from tkinter import * 
import datetime

#import strftime to retrieve system's time
from time import strftime

#to create tkinter window
root = Tk()
root.title("Digital_clock")

#lavel date time in the tkinter window
def date_time_clock():
    string = strftime('%I : %M : %S %p \n %d %B %Y \n %A')
    lbl.config(text=string)
    lbl.after(1000,date_time_clock)


#styling tkinter window
lbl = Label(font=('Calisto MT', 40,'bold'),
            bg='black',
            foreground='white') 

#placeing tkinter window in the middle
lbl.pack(anchor='center') 

#call date_time_clock function
date_time_clock()

mainloop() 