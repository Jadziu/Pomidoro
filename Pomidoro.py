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

    def main(self):
        """Main GUI body"""
        # Gui start.
        self.root.title('Pomidoro')
        self.root.resizable(width=False, height=False)

        # Creating body
        body1 = Frame(self.root, width=600, height=50, bg=bg_color)
        body1.grid(row=0, column=0, columnspan=2, sticky='nesw')
        body1.grid_propagate(False)

        body2 = Frame(self.root, width=600, height=200, bg=bg_color)
        body2.grid(row=1, column=0, columnspan=2, sticky='nesw')
        body2.grid_propagate(False)

        body3 = Frame(self.root, width=600, height=100, bg=bg_color)
        body3.grid(row=2, column=0, columnspan=2, sticky='nesw')
        body3.grid_propagate(False)

        # ROW:0 time
        time_txt = Label(body1, text='TIME: ', font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
        time_txt.grid(row=0, column=0)
        self.time_lbl = Label(body1, font=("DS-digital", 40, 'bold'), bg=bg_color, fg=fg_color)
        self.time_lbl.grid(row=0, column=1)
        self.time_now()

        self.root.mainloop()


if __name__ == '__main__':
    pomo = Pomidoro(Tk())
    pomo.main()
