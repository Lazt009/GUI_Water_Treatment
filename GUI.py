import tkinter as tk
# from readCSV import getLatestData
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
# import graphPlot as gplot


def PlotGraph(col):
    data = pd.read_csv("sensor_readings.csv")

    # process date time
    dateTime = []
    for date, time in zip(data["date"], data["time"]):
        # print(date, time)
        year, month, day = map(int, date.split("-"))
        hour, minute, second = map(int, time.split(":"))
        dateTime.append(datetime.datetime(
            year, month, day, hour, minute, second))

    # To set Figure size
    plt.figure(figsize=(9, 4))

    # To plot graph, with datetime as x value and specified param as y value
    plt.plot(dateTime, data[col], marker='.')
    plt.title("{} Graph".format(col))
    plt.xlabel("Date and Time")
    plt.ylabel(col)

    plt.show()
    # print("Graph Done")


# PlotGraph("PH")


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
BFFamily = "Verdana"
BFont = (BFFamily, BFSize)
pad = 7
pad2 = 2


# frame 1
frame1 = tk.Frame(master=window, width=800, height=140, bg="#272727")
frame1.grid(row=0, sticky="nsew", padx=5, pady=5)

frame1.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=23)
frame1.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                        10, 11], weight=1, minsize=50)
#
info = tk.Button(master=frame1, text="info", bg=color3)
info.grid(row=1, column=0, rowspan=3, columnspan=2, sticky="nsew")

nt = tk.Label(master=frame1, text="", bg=BGcolor)
nt.grid(row=2, column=2, rowspan=2, sticky="nsew")

heading = tk.Label(master=frame1, text="Water Quality Monitoring",
                   bg="#272727", fg="#14A76C", borderwidth=0, font=("Verdana", 24))
heading.grid(row=0, column=3, rowspan=2, columnspan=6,
             sticky="nsew", padx=pad, pady=pad)


logoImg = tk.PhotoImage(file="logo.png")
logo = tk.Label(frame1, image=logoImg, bg=BGcolor)
logo.grid(row=2, column=4, rowspan=4, columnspan=4,
          ipadx=1, ipady=1, sticky="nsew")

nt = tk.Label(master=frame1, text="", bg=BGcolor)
nt.grid(row=2, column=9, rowspan=2, sticky="nsew")

current = tk.Label(master=frame1, text="Current Time", bg="white")
current.grid(row=0, column=10, columnspan=2, sticky="nsew")

timeDate = tk.Label(master=frame1, bg="pink")
timeDate.grid(row=1, column=10, rowspan=2, columnspan=2, sticky="nsew")
currentTime()

lstRead = tk.Label(master=frame1, text="Last Reading", bg="white")
lstRead.grid(row=3, column=10, columnspan=2, sticky="nsew")

d = data["date"][lastIndex]
t = data["time"][lastIndex]
lstRead = tk.Label(
    master=frame1, text="Date : {}\nTime : {}".format(d, t), bg="green")
lstRead.grid(row=4, column=10, rowspan=2, columnspan=2, sticky="nsew")

# frame 2
frame2 = tk.Frame(master=window, width=800, height=140,
                  borderwidth=5, bg=color1)
frame2.grid(row=1, sticky="nsew", padx=5, pady=5)

frame2.rowconfigure([0], weight=1, minsize=80)
frame2.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=120)

p = data["PH"][lastIndex]
txt = "PH\n{}".format(p)
data1 = tk.Button(master=frame2, text=txt, bg=color4,
                  font=BFont, command=lambda: PlotGraph("PH"))
data1.grid(row=0, column=0, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)

p = data["RTD"][lastIndex]
txt = "RTD\n{}".format(p)
data2 = tk.Button(master=frame2, text=txt, bg=color4,
                  font=BFont, command=lambda: PlotGraph("RTD"))
data2.grid(row=0, column=1, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)

p = data["ORP"][lastIndex]
txt = "ORP\n{}".format(p)
data3 = tk.Button(master=frame2, text=txt, bg=color4,
                  font=BFont, command=lambda: PlotGraph("ORP"))
data3.grid(row=0, column=2, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)

p = data["DO"][lastIndex]
txt = "DO\n{}".format(p)
data4 = tk.Button(master=frame2, text=txt, bg=color4,
                  font=BFont, command=lambda: PlotGraph("DO"))
data4.grid(row=0, column=3, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)

p = data["EC"][lastIndex]
txt = "EC\n{}".format(p)
data5 = tk.Button(master=frame2, text=txt, bg=color4,
                  font=BFont, command=lambda: PlotGraph("EC"))
data5.grid(row=0, column=4, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)

p = data["F"][lastIndex]
txt = "F\n{}".format(p)
data6 = tk.Button(master=frame2, text=txt, bg=color4,
                  font=BFont, command=lambda: PlotGraph("F"))
data6.grid(row=0, column=5, sticky="nsew",
           padx=pad, pady=pad, ipadx=5, ipady=5)


# frame 3
frame3 = tk.Frame(master=window, width=800, height=200, bg=color1)
frame3.grid(row=2, sticky="nsew", padx=10, pady=10)

frame3.rowconfigure([0], weight=1, minsize=200)
frame3.columnconfigure([0, 1, 2, 3], weight=1, minsize=200)

block1 = tk.Label(master=frame3, text="Chemical\nPullutants",
                  bg=color2, font=BFont)
block1.grid(row=0, column=0, padx=pad2, pady=pad2, sticky="nsew")

block2 = tk.Label(master=frame3, text="Plastic\nDetection",
                  bg=color3,  font=BFont)
block2.grid(row=0, column=1, padx=pad2, pady=pad2, sticky="nsew")

block3 = tk.Label(master=frame3, text="Micro-\nOrganizms",
                  bg=color2,  font=BFont)
block3.grid(row=0, column=2, padx=pad2, pady=pad2, sticky="nsew")

block4 = tk.Label(master=frame3, text="Water\nQuality",
                  bg=color3,  font=BFont)
block4.grid(row=0, column=3, padx=pad2, pady=pad2, sticky="nsew")

window.mainloop()
