from time import strftime
from tkinter import *

bg_color = "#db3939"
fg_color = '#052a61'

# Initiation GUI
root = Tk()
root.title('Pomidoro')
root.resizable(width=False, height=False)

# Creating body
body = Frame(root, width=600, height=200, bg=bg_color)
body.grid(row=0, column=0, columnspan=2, sticky='nesw')
body.grid_propagate(False)


def time_now():
    """Get local time, config in label, update time"""
    global mytime
    mytime = strftime('%H:%M:%S')
    time_lbl.config(text=mytime)
    time_lbl.after(500, time_now)


time_txt = Label(body, text='TIME: ', font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
time_txt.grid(row=0, column=0)
time_lbl = Label(body, font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
time_lbl.grid(row=0, column=1)
time_now()

root.mainloop()
