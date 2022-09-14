from time import strftime, clock_gettime
from tkinter import *

root = Tk()
root.title('Pomidoro')


def time():
    mytime = strftime('%Z %H:%M:%S')
    mytime2 = clock_gettime()
    mylbl.config(text=mytime)
    mylbl2.config(text=mytime2)
    mylbl.after(500, time)
    mylbl2.after(500, time)


mylbl = Label(root, font=("Arial", 72, 'bold'))
mylbl.pack()
mylbl2 = Label(root, font=("Arial", 72, 'bold'))
mylbl2.pack()
time()

root.mainloop()