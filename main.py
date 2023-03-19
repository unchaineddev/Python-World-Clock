FONT = ("times", 20, "bold")
FONTS = ("times", 25, "bold")


from datetime import datetime
import pytz
from tkinter import *
import time



root = Tk()
root.title("World Clock")
root.geometry("500x250")


def times():
    home=pytz.timezone('Asia/Kolkata')
    local_time=datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text="India")
    clock1.after(200, times)


    home=pytz.timezone('America/Los_Angeles')
    local_time=datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text="United States")
    clock2.after(200, times)


    home=pytz.timezone('Europe/London')
    local_time=datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text="London")
    clock3.after(200, times)


    home=pytz.timezone('Australia/Adelaide')
    local_time=datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock4.config(text=current_time)
    name4.config(text="Australia")
    clock4.after(200, times)

name1 = Label(root, font=FONT)
name1.place(x=30, y=5)
clock1 = Label(root,  font=FONTS)
clock1.place(x=10, y=40)
world1 = Label(root, text="Hours  minutes     seconds", font="times 10 bold")
world1.place(x=10, y=80)


name2 = Label(root, font=FONT)
name2.place(x=330, y=5)
clock2 = Label(root, font=FONTS)
clock2.place(x=310, y=40)
world2 = Label(root, text="Hours  minutes     seconds", font="times 10 bold")
world2.place(x=310, y=80)


name3 = Label(root, font=FONT)
name3.place(x=30, y=105)
clock3 = Label(root, font=FONTS)
clock3.place(x=10, y=140)
world3 = Label(root, text="Hours  minutes     seconds", font="times 10 bold")
world3.place(x=10, y=180)




name4 = Label(root, font=FONT)
name4.place(x=330, y=105)
clock4 = Label(root,  font=FONTS)
clock4.place(x=310, y=140)
world4 = Label(root, text="Hours  minutes     seconds", font="times 10 bold")
world4.place(x=310, y=180)


times()


root.mainloop()



##### HOW TO GET TIME ZONE  #####
#####                       #####
# for tz in pytz.all_timezones:
#     print(tz)all_timezones


# home=pytz.timezone('Australia/Victoria')
# local_time=datetime.now(home)
# current_time = local_time.strftime("%H:%M:%S")
# print(current_time)


