Created on Thu Nov 17 11:23:05 2022

@author: 15129
"""


from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Label

root = Tk()

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





root.geometry("800x800")
root.title("Groundstation UI")
root.mainloop()
