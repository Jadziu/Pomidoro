from time import strftime
from tkinter import *

bg_color = "#db3939"
fg_color = '#052a61'


class Pomidoro:
    def __init__(self, root):
        self.root = root

    def time_now(self):
        """Get local time, config in label, update time"""
        mytime = strftime('%H:%M:%S')
        self.time_lbl.config(text=mytime)
        self.time_lbl.after(500, self.time_now)

    def colon(self):
        """Make colon def for less code"""
        self.timer_colon = Label(self.body2, text=':', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)

    def main(self):
        """Main GUI body"""
        # Gui start.
        self.root.title('Pomidoro')
        self.root.resizable(width=False, height=False)

        # Creating body
        body1 = Frame(self.root, width=600, height=50, bg=bg_color)
        body1.grid(row=0, column=0, columnspan=2, sticky='nesw')
        body1.grid_propagate(False)

        self.body2 = Frame(self.root, width=600, height=200, bg=bg_color)
        self.body2.grid(row=1, column=0, columnspan=2, sticky='nesw')
        self.body2.grid_propagate(False)

        body3 = Frame(self.root, width=600, height=100, bg=bg_color)
        body3.grid(row=2, column=0, columnspan=2, sticky='nesw')
        body3.grid_propagate(False)

        # ROW:0 time
        time_txt = Label(body1, text='TIME: ', font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
        time_txt.grid(row=0, column=0)
        self.time_lbl = Label(body1, font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
        self.time_lbl.grid(row=0, column=1)
        self.time_now()

        # ROW:1 timer one
        # veriables:
        self.hr1 = StringVar()
        self.hr1.set('00')
        self.mins1 = StringVar()
        self.mins1.set('00')
        self.secs1 = StringVar()
        self.secs1.set('00')

        # TIMER1 title
        timer1_txt = Label(self.body2, text='TIMER1: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
        timer1_txt.grid(row=1, column=0, sticky='nw')

        # T1 hours
        timer1_hr = Entry(self.body2, textvariable=self.hr1, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                          width=2, relief='flat')
        timer1_hr.grid(row=1, column=1, sticky='nw')
        self.colon()
        self.timer_colon.grid(row=1, column=2, sticky='nw')

        # T1 minutes
        timer1_min = Entry(self.body2, textvariable=self.mins1, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                           width=2, relief='flat')
        timer1_min.grid(row=1, column=3, sticky='nw')
        self.colon()
        self.timer_colon.grid(row=1, column=4, sticky='nw')

        # T1 seconds
        timer1_sec = Entry(self.body2, textvariable=self.secs1, font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color,
                           width=2, relief='flat')
        timer1_sec.grid(row=1, column=5, sticky='nw')

        # TIMER2 title
        timer2_txt = Label(self.body2, text='TIMER2: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
        timer2_txt.grid(row=2, column=0, sticky='nw')

        self.root.mainloop()


if __name__ == '__main__':
    pomo = Pomidoro(Tk())
    pomo.main()
