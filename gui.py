# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:23:05 2022

@author: 15129
"""


from tkinter import *
from tkinter import ttk
from tkinter.ttk import  Label
from subprocess import*
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import  NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np
from tkinter import filedialog
import pandas as pd
import globe
import satList
import move
import tracking
import pandas as pd
from pandas import DataFrame



root = Tk()
root.wm_title("Groundstation GUI")

elevation = 0
asythmith = 0

#Set Up the Different Tabs on the GUI
tabs = ttk.Notebook(root, padding= 20)
tabs.pack(fill=BOTH, expand=TRUE)
userControlFrame = ttk.Frame(tabs)
visualFrame = ttk.Frame(tabs)
dataRecivedFrame = ttk.Frame(tabs)
satListFrame = ttk.Frame(tabs)
tabs.add(userControlFrame, text="Manual Control")
tabs.add(visualFrame, text="View of the Sat")
tabs.add(dataRecivedFrame, text="Data Recived")
tabs.add(satListFrame, text="Sat List")

# Data Recieved

#Manual Control Tab

button1=ttk.Button(userControlFrame, text="Up", command=move.up)
button1.grid(row=10,column=20)

button2=ttk.Button(userControlFrame, text="Down", command=move.down)
button2.grid(row=30,column=20)

button3=ttk.Button(userControlFrame, text="Left",command=move.left)
button3.grid(row=20,column=10)

button4=ttk.Button(userControlFrame, text="Right", command= move.right)
button4.grid(row=20,column=30)

button5=ttk.Button(userControlFrame, text="Auto Tracking", command=tracking.autoTrack)
button5.grid(row=50,column=50)



#View of the Sat

isometricview = Button(visualFrame, command = globe.globe(visualFrame), text = "globe")


#Sat List
button6=ttk.Button(satListFrame ,text="Open Sat Table", command = satList.openFile(satListFrame))
button6.grid(row=50,column=50)








root.mainloop()
