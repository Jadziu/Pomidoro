import time
from time import strftime
from tkinter import *

bg_color = "#db3939"
fg_color = '#052a61'
counting = False


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

    def clear(self):
        """Clear timers"""
        if not self.counting:
            self.mins1.set('00')
            self.secs1.set('00')
            self.mins2.set('00')
            self.secs2.set('00')
            print("Timers cleared")
        else:
            print("Timers running...")

    def start(self):
        """Counting time down. Not used "sleep" function."""
        # Get time, timer, prepare for countdown.
        gettime = (time.time_ns() / 1000000000)
        timenow = gettime
        sec1 = self.secs1.get()
        min1 = self.mins1.get()
        sec2 = self.secs2.get()
        min2 = self.mins2.get()

        # Set "stop" flag
        self.counting = True

        # convert minutes and seconds to "one number".
        counter1 = int(sec1) + (int(min1) * 60)
        counter2 = int(sec2) + (int(min2) * 60)

        # Countdown loops.
        print("Start counting timers")
        print(f"Timer1: {min1} min, {sec1} sec.")
        print(f"Timer2: {min2} min, {sec2} sec.")

        while counter1 > 0:
            gettime = (time.time_ns() / 1000000000)
            if (gettime - timenow) >= 1:
                timenow = gettime
                counter1 -= 1

                # Use divmod to change "one number" to minutes and seconds.
                up_min, up_sec = divmod(counter1, 60)
                self.secs1.set(str("%02d" % up_sec ))
                self.mins1.set(str("%02d" % up_min))

            # Update GUI (IMPORTANT!!!!)
            self.root.update()

            # Check "stop" flag.
            if not self.counting:
                break

        while counter2 > 0 and counter1 == 0:
            gettime = (time.time_ns() / 1000000000)
            if (gettime - timenow) >= 1:
                timenow = gettime
                counter2 -= 1

                # Use divmod to change "one number" to minutes and seconds.
                up_min, up_sec = divmod(counter2, 60)
                self.secs2.set(str("%02d" % up_sec))
                self.mins2.set(str("%02d" % up_min))

            # Update GUI (IMPORTANT!!!!)
            self.root.update()

            # Check "stop" flag.
            if not self.counting:
                break

        print("Counting ended")

    def stop(self):
        """Stop counting"""
        # Set "stop" flag.
        self.counting = False
        print("Counting stoped")

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
        self.mins1 = StringVar()
        self.mins1.set('00')
        self.secs1 = StringVar()
        self.secs1.set('00')

        # TIMER1 title
        timer1_txt = Label(self.body2, text='TIMER1: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
        timer1_txt.grid(row=1, column=0, sticky='nw')

        # T1 minutes
        timer1_min = Entry(self.body2, textvariable=self.mins1, font=("DS-digital", 60, 'bold'), bg=bg_color,
                           fg=fg_color, width=2, relief='flat')
        timer1_min.grid(row=1, column=1, sticky='nw')
        self.colon()
        self.timer_colon.grid(row=1, column=2, sticky='nw')

        # T1 seconds
        timer1_sec = Entry(self.body2, textvariable=self.secs1, font=("DS-digital", 60, 'bold'), bg=bg_color,
                           fg=fg_color, width=2, relief='flat')
        timer1_sec.grid(row=1, column=3, sticky='nw')

        # ROW:2 timer two
        # veriables:
        self.mins2 = StringVar()
        self.mins2.set('00')
        self.secs2 = StringVar()
        self.secs2.set('00')

        # TIMER2 title
        timer2_txt = Label(self.body2, text='TIMER2: ', font=("DS-digital", 60, 'bold'), bg=bg_color, fg=fg_color)
        timer2_txt.grid(row=2, column=0, sticky='nw')

        # T2 minutes
        timer2_min = Entry(self.body2, textvariable=self.mins2, font=("DS-digital", 60, 'bold'), bg=bg_color,
                           fg=fg_color, width=2, relief='flat')
        timer2_min.grid(row=2, column=1, sticky='nw')
        self.colon()
        self.timer_colon.grid(row=2, column=2, sticky='nw')

        # T2 seconds
        timer2_sec = Entry(self.body2, textvariable=self.secs2, font=("DS-digital", 60, 'bold'), bg=bg_color,
                           fg=fg_color, width=2, relief='flat')
        timer2_sec.grid(row=2, column=3, sticky='nw')

        # MODE SELECTION:

        # START BUTTON:
        start_btn = Button(body3, text='START', font=("DS-digital", 30, 'bold'), command=self.start)
        start_btn.grid(row=3, column=0, padx=20)

        # STOP BUTTON:
        stop_btn = Button(body3, text='STOP', font=("DS-digital", 30, 'bold'), command=self.stop)
        stop_btn.grid(row=3, column=1, padx=20)

        # STOP BUTTON:
        clear_btn = Button(body3, text='CLEAR', font=("DS-digital", 30, 'bold'), command=self.clear)
        clear_btn.grid(row=3, column=3, padx=20)

        self.root.mainloop()


if __name__ == '__main__':
    pomo = Pomidoro(Tk())
    pomo.main()
