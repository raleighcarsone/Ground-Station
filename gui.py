# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:23:05 2022

@author: 15129
"""

import tkinter
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
#define functions used in the gui
def openFile():

   filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
("All Files", "*.")))

   if filename:
      try:
         filename = r"{}".format(filename)
         df = pd.read_excel(filename)
      except ValueError:
         label.config(text="File could not be opened")
      except FileNotFoundError:
         label.config(text="File Not Found")

   # Clear all the previous data in tree
   clear_treeview()

   # Add new data in Treeview widget
   tree["column"] = list(df.columns)
   tree["show"] = "headings"

   # For Headings iterate over the columns
   for col in tree["column"]:
      tree.heading(col, text=col)

   # Put Data in Rows
   df_rows = df.to_numpy().tolist()
   for row in df_rows:
         tree.insert("", "end", values=row)

   tree.pack()


# Clear the Treeview Widget
def clear_treeview():
   tree.delete(*tree.get_children())



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
button1.place(y=50,x=100)

button2=ttk.Button(userControlFrame, text="Down", command=move.down)
button2.place(y=100,x=100)

button3=ttk.Button(userControlFrame, text="Left",command=move.left)
button3.place(y=100,x=0)

button4=ttk.Button(userControlFrame, text="Right", command= move.right)
button4.place(y=100,x=200)

button5=ttk.Button(userControlFrame, text="Auto Tracking", command=tracking.autoTrack)
button5.place(y=0,x=0)



#View of the Sat

isometricview = Button(visualFrame, command = globe.globe(visualFrame), text = "globe")


#Sat List
tree = ttk.Treeview(satListFrame)
tree.place(y=50)
tree.pack(expand=tkinter.TRUE)


button6=ttk.Button(satListFrame ,text="Open Sat Table", command = openFile)
button6.place(y=0,x=0)

root.mainloop()
