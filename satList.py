# -*- coding: utf-8 -*-
#def importData():
 #   import pandas as pd
 #   satList = pd.read_excel(r'C:\Users\15129\Downloads\satList.xlsx')
#if __name__ == "__importData__":
  #  importData()




# Import the required libraries
from tkinter import *
from tkinter import ttk, filedialog
import numpy
import pandas as pd



tree = ttk.Treeview()

def openFile(frame):
   tree = ttk.Treeview(frame)

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


