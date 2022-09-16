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

body2 = Frame(root, width=600, height=200, bg=bg_color)
body2.grid(row=1, column=0, columnspan=2, sticky='nesw')
body2.grid_propagate(False)

body3 = Frame(root, width=600, height=100, bg=bg_color)
body3.grid(row=2, column=0, columnspan=2, sticky='nesw')
body3.grid_propagate(False)


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


def clear():
    hr1.set('00')
    mins1.set('00')
    secs1.set('00')





# ROW:0 time
time_txt = Label(body1, text='TIME: ', font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
time_txt.grid(row=0, column=0)
time_lbl = Label(body1, font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
time_lbl.grid(row=0, column=1)
time_now()

# ROW:1 timer one
# veriables:
hr1 = StringVar()
hr1.set('00')
mins1 = StringVar()
mins1.set('00')
secs1 = StringVar()
secs1.set('00')

# TIMER title
timer1_txt = Label(body2, text='TIMER1: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
timer1_txt.grid(row=1, column=0, sticky='nw')

# T1 hours
timer1_hr = Entry(body2, textvariable=hr1, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                  width=2, relief='flat')
timer1_hr.grid(row=1, column=1, sticky='nw')
colon()
timer_colon.grid(row=1, column=2, sticky='nw')


# T1 minutes
timer1_min = Entry(body2, textvariable=mins1, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer1_min.grid(row=1, column=3, sticky='nw')
colon()
timer_colon.grid(row=1, column=4, sticky='nw')

# T1 seconds
timer1_sec = Entry(body2, textvariable=secs1, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer1_sec.grid(row=1, column=5, sticky='nw')

# ROW:2 timer two
# veriables:
hr2 = StringVar()
hr2.set('00')
mins2 = StringVar()
mins2.set('00')
secs2 = StringVar()
secs2.set('00')

# TIMER title
timer2_txt = Label(body2, text='TIMER2: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
timer2_txt.grid(row=2, column=0, sticky='nw')

# T1 hours
timer2_hr = Entry(body2, textvariable=hr2, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                  width=2, relief='flat')
timer2_hr.grid(row=2, column=1, sticky='nw')
colon()
timer_colon.grid(row=2, column=2, sticky='nw')

# T1 minutes
timer2_min = Entry(body2, textvariable=mins2, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer2_min.grid(row=2, column=3, sticky='nw')
colon()
timer_colon.grid(row=2, column=4, sticky='nw')

# T1 seconds
timer2_sec = Entry(body2, textvariable=secs2, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                   width=2, relief='flat')
timer2_sec.grid(row=2, column=5, sticky='nw')

# MODE SELECTION:

# START BUTTON:
start_btn = Button(body3, text='START', font=("DS-digital", 30, 'bold'))
start_btn.grid(row=3, column=0, padx=20)

stop_btn = Button(body3, text='STOP', font=("DS-digital", 30, 'bold'))
stop_btn.grid(row=3, column=1, padx=20)

clear_btn = Button(body3, text='CLEAR', font=("DS-digital", 30, 'bold'), command=clear)
clear_btn.grid(row=3, column=3, padx=20)


root.mainloop()
