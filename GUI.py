import tkinter as tk

window = tk.Tk()

#Configuration of rows
window.rowconfigure([0, 1, 2], weight=1)
window.columnconfigure(0, weight=1, minsize=50)
window.title("Water quality monitoring")

#frame 1
frame1 = tk.Frame(master=window, width=800, height=140, bg="red")
frame1.grid(row=0, sticky="nsew")

frame1.rowconfigure([0,1,2,3,4,5], weight=1, minsize=23)
frame1.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11], weight=1, minsize=66)
#
info = tk.Button(master=frame1, text="info")
info.grid(row=1, column=0, rowspan=3, columnspan=2, sticky="nsew" )

nt = tk.Label(master=frame1, text="nothing")
nt.grid(row=2, column=2, rowspan=2, sticky="nsew" )

heading = tk.Label(master=frame1, text="Water Quality Treatment", bg="pink", font=("Arial", 30) )
heading.grid(row=0, column=3, rowspan=2, columnspan=6, sticky="nsew")

logoImg = tk.PhotoImage(file="logo.png")
logo = tk.Label(frame1, image=logoImg, bg="red")
logo.grid(row=2, column=4, rowspan=4, columnspan=4,sticky="nsew")

nt = tk.Label(master=frame1, text="nothing")
nt.grid(row=2, column=9, rowspan=2, sticky="nsew" )

timeDate = tk.Label(master=frame1, text="Time:\nDate:", bg="pink")
timeDate.grid(row=1, column=10, rowspan=3, columnspan=2, sticky="nsew")

#frame 2
frame2 = tk.Frame(master=window, width=800, height=140, bg="blue")
frame2.grid(row=1, sticky="nsew")

frame2.rowconfigure([0], weight=1, minsize=140)
frame2.columnconfigure([0,1,2,3,4,5], weight=1, minsize=133)

data1 = tk.Label(master=frame2, text="data1", bg="red")
data1.grid(row=0, column=0, sticky="nsew")

data2 = tk.Label(master=frame2, text="data2", bg="orange")
data2.grid(row=0, column=1, sticky="nsew")

data3 = tk.Label(master=frame2, text="data3", bg="yellow")
data3.grid(row=0, column=2, sticky="nsew")

data4 = tk.Label(master=frame2, text="data4", bg="green")
data4.grid(row=0, column=3, sticky="nsew")

data5 = tk.Label(master=frame2, text="data5", bg="Indigo")
data5.grid(row=0, column=4, sticky="nsew")

data6 = tk.Label(master=frame2, text="data6", bg="blue")
data6.grid(row=0, column=5, sticky="nsew")


#frame 3
frame3 = tk.Frame(master=window, width=800, height=200, bg="green")
frame3.grid(row=2, sticky="nsew")

frame3.rowconfigure([0], weight=1, minsize=200)
frame3.columnconfigure([0,1,2,3], weight=1, minsize=200)

block1 = tk.Label(master=frame3, text="block1", bg="blue")
block1.grid(row=0, column=0, sticky="nsew")

block2 = tk.Label(master=frame3, text="block2", bg="Indigo")
block2.grid(row=0, column=1, sticky="nsew")

block3 = tk.Label(master=frame3, text="block3", bg="green")
block3.grid(row=0, column=2, sticky="nsew")

block4 = tk.Label(master=frame3, text="block4", bg="yellow")
block4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
