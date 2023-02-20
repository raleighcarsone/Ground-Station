# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:51:47 2023

@author: 15129
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:23:05 2022
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:23:05 2022

Groundstation GUI
"""

import threading
import tkinter as tk
from tkinter import ttk, filedialog
from subprocess import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np
import pandas as pd
import globe
import satList
import move
import tracking

def openFile():
    filename = filedialog.askopenfilename(
        title="Open a File",
        filetype=(("xlxs files", "*.xlsx"), ("All Files", "*.*"))
    )

    if filename:
        try:
