# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:27:23 2022

@author: 15129
"""
import sys
def globe(tab):
    import os
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    
    os.environ['PROJ_LIB'] = '/Users/mb/anaconda3/envs/worklab/share/proj' 
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    import numpy as np
    
    fig = plt.figure(figsize=(9,6))
    
    # set perspective angle
    lat_viewing_angle = 10
    lon_viewing_angle = -73
    
    # define color maps for water and land
    ocean_map = (plt.get_cmap('ocean'))(210)
    cmap = plt.get_cmap('gist_earth')
    
    # call the basemap and use orthographic projection at viewing angle
    m = Basemap(projection='ortho', 
              lat_0=lat_viewing_angle, lon_0=lon_viewing_angle)    
    
    # coastlines, map boundary, fill continents/water, fill ocean, draw countries
    m.drawcoastlines()
    m.drawmapboundary(fill_color=ocean_map)
    m.fillcontinents(color=cmap(200),lake_color=ocean_map)
    m.drawcountries()
    
    # latitude/longitude line vectors
    lat_line_range = [-90,90]
    lat_lines = 8
    lat_line_count = (lat_line_range[1]-lat_line_range[0])/lat_lines
    
    merid_range = [-180,180]
    merid_lines = 8
    merid_count = (merid_range[1]-merid_range[0])/merid_lines
    
    m.drawparallels(np.arange(lat_line_range[0],lat_line_range[1],lat_line_count))
    m.drawmeridians(np.arange(merid_range[0],merid_range[1],merid_count))
    
       # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,tab)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, tab)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
if __name__ == "__globe__":
    globe(sys.argv[1])