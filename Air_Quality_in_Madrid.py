from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.filedialog import askopenfilename
import urllib.request
from PIL import Image


def close_window():
    win.destroy()

def graphs():
    label.pack_forget()
    button3.pack_forget()
    t1.pack_forget()
    t2.pack_forget()
    t3.pack_forget()
    t4.pack_forget()
    t5.pack_forget()
    t6.pack_forget()
    hello.pack_forget()


    button4 = Button(win, text = 'Close', command = close_window)
    button4.pack(fill=X, padx=3, pady=3, ipadx=3, ipady=3)

    csv_file_path = askopenfilename()

    start_date = dt.datetime(2017, 1, 1)
    end_date = dt.datetime(2018, 1, 1)
    daterange = pd.date_range(start_date, end_date)
    user_csv = pd.read_csv(csv_file_path)
    NO_2_levels = user_csv['NO_2'].tolist()
    df = pd.DataFrame(NO_2_levels, index=daterange, columns=["NO_2_levels"])
    df.loc["Jan 01 2017":"Jan 01 2018"].plot()
    figure1 = plt.Figure(figsize=(10,10), dpi=60)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, win)
    bar1.get_tk_widget().pack(fill=X)
    df.plot(kind='line', legend=True, ax=ax1)
    ax1.set_title('NO_2 Concentration levels in 2017')




win = Tk()
win.title("Pollution in Madrid")
win.geometry('500x800')
win.configure(background="light yellow")

hello=Label(win, text="WELCOME!", bg="light yellow")
hello.pack(padx=3, pady=3, ipadx=3, ipady=3, fill=X)

t1=Label(win, text="This program will allow you to check for NO_2 levels",bg="light yellow")
t1.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=X)
t2=Label(win, text="in the desired stations in Madrid during 2017.",bg="light yellow")
t2.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=X)
t3=Label(win,bg="light yellow")
t3.pack(padx=0.5, pady=0.5, ipadx=0.5, ipady=0.5, fill=X)
t4=Label(win, text="The file that you are going to insert should contain the NO_2 level",bg="light yellow")
t4.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=X)
t5=Label(win, text="per day in one column under the name 'NO_2' and the days",bg="light yellow")
t5.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=X)
t6=Label(win, text="from Jan 01 2017 to Jan 01 2018 in the other column.",bg="light yellow")
t6.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=X)

def getImage():
    link = "https://i.imgur.com/dgP95Sl.png"
    image = Image.open(urllib.request.urlopen(link))
    image.save("temp.png")

getImage()
mapa=PhotoImage(file = "temp.png")
mapa=mapa.subsample(3,3)
label=Label(image=mapa)
label.place(x=0,y=0, relwidth=1.0, relheight=1.0)
label.pack()


button3= Button(win, text = 'Open File', command = graphs)
button3.pack(fill=X,padx=3, pady=3, ipadx=3, ipady=3)
win.mainloop()
