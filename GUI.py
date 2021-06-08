import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from graphPlot import plotGraph
from DebugWindow import childWindow
from info import infoWindow


def currentTime():
    dt = datetime.datetime.now()
    d = dt.strftime("%Y-%m-%d")
    t = dt.strftime("%H:%M:%S")
    timeDate.config(text="Date : {}\nTime : {}".format(d, t))
    timeDate.after(1000, currentTime)


# reading data
data = pd.read_csv("sensor_readings.csv")

lastIndex = len(data) - 1


window = tk.Tk()

# Configuration of rows
window.config(bg='#272727')
window.rowconfigure([0, 1, 2], weight=1)
window.columnconfigure(0, weight=1, minsize=50)
window.title("Water quality monitoring")
window.geometry("800x480")
# black
BGcolor = "#272727"

# grey
color1 = "#747474"

# red
color2 = "#FF652F"

# yellow
color3 = "#FFE400"

# green
color4 = "#14A76C"

BFSize = 15
BFFamily = "Verdana BOLD"
BFont = (BFFamily, BFSize)

BFont2=(BFFamily,16)
pad = 7
pad2 = 2







# ==========================================================

# frame 1
frame1 = tk.Frame(master=window, width=800, height=140, bg=BGcolor)
frame1.grid(row=0, sticky="nsew", padx=5, pady=5)

frame1.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=23)
frame1.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                        10, 11], weight=1, minsize=50)




# ----------------



lstRead = tk.Label(master=frame1, text="Last Reading", bg=color2)
lstRead.grid(row=0, column=0, columnspan=2, sticky="nsew", )

d = data["date"][lastIndex]
t = data["time"][lastIndex]
lstRead = tk.Label(
    master=frame1, text="Date : {}\nTime : {}".format(d, t), bg=color2)
lstRead.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="nsew")

info = tk.Button(master=frame1, text="Info", fg=color4,command=lambda: infoWindow(window))
info.grid(row=3, column=3, sticky="nsew")


heading = tk.Label(master=frame1, text="Water Quality Monitoring",
                   bg=BGcolor, fg=color4, borderwidth=0, font=("Verdana", 24))
heading.grid(row=0, column=3, rowspan=2, columnspan=6,
             sticky="nsew", padx=pad, pady=pad)

debug = tk.Button(master=frame1, text="Debug", fg=color4,command=lambda: childWindow(window))
debug.grid(row=3, column=8, sticky="nsew")

logoImg = tk.PhotoImage(file="logo.png")
logo = tk.Label(frame1, image=logoImg, bg=BGcolor)
logo.grid(row=2, column=4, rowspan=4, columnspan=4,
          ipadx=1, ipady=1, sticky="nsew")

current = tk.Label(master=frame1, text="Current Time", bg=color2)
current.grid(row=0, column=10, columnspan=2, sticky="nsew")

timeDate = tk.Label(master=frame1, bg=color2)
timeDate.grid(row=1, column=10, rowspan=2, columnspan=2, sticky="nsew")
currentTime()










# =================================================================

# frame 2
frame2 = tk.Frame(master=window, width=800, height=140,
                  borderwidth=5, bg=color1)
frame2.grid(row=1, sticky="nsew", padx=5, pady=5)

frame2.rowconfigure([0], weight=1, minsize=80)
frame2.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=120)





#-----------

p = data["PH"][lastIndex]
txt = "PH\n{}".format(p)
data_ph = tk.Button(master=frame2, text=txt, fg=color4,
                  font=BFont, command=lambda: plotGraph("PH"))
data_ph.grid(row=0, column=0, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)


p = data["RTD"][lastIndex]
txt = "RTD\n{}".format(p)
data_rtd = tk.Button(master=frame2, text=txt, fg=color4,
                  font=BFont, command=lambda: plotGraph("RTD"))
data_rtd.grid(row=0, column=1, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)


p = data["ORP"][lastIndex]
txt = "ORP\n{}".format(p)
data_orp = tk.Button(master=frame2, text=txt, fg=color4,
                  font=BFont, command=lambda: plotGraph("ORP"))
data_orp.grid(row=0, column=2, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)


p = data["DO"][lastIndex]
txt = "DO\n{}".format(p)
data_do = tk.Button(master=frame2, text=txt, fg=color4,
                  font=BFont, command=lambda: plotGraph("DO"))
data_do.grid(row=0, column=3, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)


p = data["EC"][lastIndex]
txt = "EC\n{}".format(p)
data_ec = tk.Button(master=frame2, text=txt, fg=color4,
                  font=BFont, command=lambda: plotGraph("EC"))
data_ec.grid(row=0, column=4, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)


p = data["F"][lastIndex]
txt = "F\n{}".format(p)
data_f = tk.Button(master=frame2, text=txt, fg="#14A76C",
                  font=BFont, command=lambda: plotGraph("F"))
data_f.grid(row=0, column=5, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)








# ================================================================


# frame 3
frame3 = tk.Frame(master=window, width=800, height=200, bg=color1)
frame3.grid(row=2, sticky="nsew", padx=10, pady=10)

frame3.rowconfigure([0], weight=1, minsize=200)
frame3.columnconfigure([0, 1, 2, 3], weight=1, minsize=200)



chemical_pollutants="Water is Acidic"
plastic_detection="L5"
micro_organisms="Present"
water_quality="Very Bad"

# -------------

block1 = tk.Label(master=frame3, text="Chemical\nPullutants\n\n\n"+chemical_pollutants,
                  bg=color2, font=BFont2)
block1.grid(row=0, column=0, padx=pad2, pady=pad2, sticky="nsew")


block2 = tk.Label(master=frame3, text="Plastic\nDetection\n\n\n",
                  bg=color3,  font=BFont2)
block2.grid(row=0, column=1, padx=pad2, pady=pad2, sticky="nsew")


block3 = tk.Label(master=frame3, text="Micro-\nOrganizms\n\n\n"+micro_organisms,
                  bg=color2,  font=BFont2)
block3.grid(row=0, column=2, padx=pad2, pady=pad2, sticky="nsew")


block4 = tk.Label(master=frame3, text="Water\nQuality\n\n\n"+water_quality,
                  bg=color3,  font=BFont2)
block4.grid(row=0, column=3, padx=pad2, pady=pad2, sticky="nsew")

window.mainloop()

# ------------





# tried and refused

# block1 = tk.Frame(master=frame3, bg=color2)
# block1.grid(row=0, column=0, padx=pad2, pady=pad2, sticky="nsew")
# block1.columnconfigure([0], weight=1,minsize=200)
# block1.rowconfigure([0, 1], weight=1, minsize=100)

# head1=tk.Label(master=block1,fg=BGcolor,bg=color2, text="Chemical \nPollutant" ,font=BFont2)
# head1.grid(row=0, padx=pad2, pady=pad2, sticky="nsew")

# chemical=tk.Label(master=block1,fg="white",bg=color2, text="Water is Acidic" ,font=BFont)
# chemical.grid(row=1, padx=pad2, pady=pad2, sticky="nsew")