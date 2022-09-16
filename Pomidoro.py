from time import strftime
from tkinter import *

bg_color = "#db3939"
fg_color = '#052a61'



# Initiation GUI
root = Tk()
root.title('Pomidoro')
root.resizable(width=False, height=False)

# Creating body
body1 = Frame(root, width=600, height=50, bg=bg_color)
body1.grid(row=0, column=0, columnspan=2, sticky='nesw')
body1.grid_propagate(False)
body2 = Frame(root, width=600, height=300, bg=bg_color)
body2.grid(row=1, column=0, columnspan=2, sticky='nesw')
body2.grid_propagate(False)


def time_now():
    """Get local time, config in label, update time"""
    global mytime
    mytime = strftime('%H:%M:%S')
    time_lbl.config(text=mytime)
    time_lbl.after(500, time_now)


def colon():
    """Make colon def for less code"""
    global timer_colon
    timer_colon = Label(body2, text=':', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)


# ROW:0 time
time_txt = Label(body1, text='TIME: ', font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
time_txt.grid(row=0, column=0)
time_lbl = Label(body1, font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
time_lbl.grid(row=0, column=1)
time_now()

# ROW:1 timer one
# veriables:
hr = StringVar()
hr.set('00')
mins = StringVar()
mins.set('00')
secs = StringVar()
secs.set('00')

# TIMER title
timer1_txt = Label(body2, text='TIMER1: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
timer1_txt.grid(row=1, column=0, sticky='nw')

# T1 hours
timer1_hr = Entry(body2, textvariable=hr, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                  width=2, relief='flat')
timer1_hr.grid(row=1, column=1, sticky='nw')
colon()
timer_colon.grid(row=1, column=2, sticky='nw')

# T1 minutes
timer1_min = Entry(body2, textvariable=mins, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer1_min.grid(row=1, column=3, sticky='nw')
colon()
timer_colon.grid(row=1, column=4, sticky='nw')

# T1 seconds
timer1_sec = Entry(body2, textvariable=secs, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer1_sec.grid(row=1, column=5, sticky='nw')

# ROW:2 timer two
# veriables:
hr = StringVar()
hr.set('00')
mins = StringVar()
mins.set('00')
secs = StringVar()
secs.set('00')

# TIMER title
timer1_txt = Label(body2, text='TIMER1: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
timer1_txt.grid(row=2, column=0, sticky='nw')

# T1 hours
timer1_hr = Entry(body2, textvariable=hr, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                  width=2, relief='flat')
timer1_hr.grid(row=2, column=1, sticky='nw')
colon()
timer_colon.grid(row=2, column=2, sticky='nw')

# T1 minutes
timer1_min = Entry(body2, textvariable=mins, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer1_min.grid(row=2, column=3, sticky='nw')
colon()
timer_colon.grid(row=2, column=4, sticky='nw')

# T1 seconds
timer1_sec = Entry(body2, textvariable=secs, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer1_sec.grid(row=2, column=5, sticky='nw')


root.mainloop()
