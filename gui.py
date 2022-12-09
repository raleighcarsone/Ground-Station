"""
Created on Thu Nov 17 11:23:05 2022

@author: 15129
"""


from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Label
from subprocess import*
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np

root = Tk()

elevation = 0
asythmith = 0

#Set Up the Different Tabs on the GUI
tabs = ttk.Notebook(root, padding= 15)
tabs.pack(fill=BOTH, expand=TRUE)
userControl = ttk.Frame(tabs)
visual = ttk.Frame(tabs)
dataRecived = ttk.Frame(tabs)
satList = ttk.Frame(tabs)
tabs.add(userControl, text="Manual Control")
tabs.add(visual, text="View of the Sat")
tabs.add(dataRecived, text="Data Recived")
tabs.add(satList, text="Sat List")

#Manual Control Tab

button1=ttk.Button(userControl, text="Up")
button1.grid(row=1,column=2)

button2=ttk.Button(userControl, text="Down")
button2.grid(row=3,column=2)

button3=ttk.Button(userControl, text="Left")
button3.grid(row=2,column=1)

button4=ttk.Button(userControl, text="Right")
button4.grid(row=2,column=3)

button5=ttk.Button(userControl, text="Auto Tracking")
button5.grid(row=5,column=5)

userControl.mainloop()


#View of the Sat




#Sat List

def func():
    proc = Popen("satList.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)


Check = Button(satList, text="Display List", command=func)
Quit = Button(satList, text="Exit", fg="red", command=root.quit)
output = Text(satList, width=40, height=8)

Check.pack(padx=20, pady=8)
Quit.pack(padx=20, pady=18)
output.pack()




root.mainloop()
