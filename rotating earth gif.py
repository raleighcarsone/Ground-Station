# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:19:51 2022

@author: 15129
"""

from gifly import gif_maker
import datetime,matplotlib,time
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# plt.ion() allows python to update its figures in real-time
plt.ion()
fig = plt.figure(figsize=(9,6))

# set the latitude angle steady, and vary the longitude. You can also reverse this to
# create a rotating globe latitudinally as well
lat_viewing_angle = [20.0,20.0]
lon_viewing_angle = [-180,180]
rotation_steps = 100
lat_vec = np.linspace(lat_viewing_angle[0],lat_viewing_angle[0],rotation_steps)
lon_vec = np.linspace(lon_viewing_angle[0],lon_viewing_angle[1],rotation_steps)

# for making the gif animation
gif_indx = 0

# define color maps for water and land
ocean_map = (plt.get_cmap('ocean'))(150)
cmap = plt.get_cmap('gist_earth')

# loop through the longitude vector above
for pp in range(0,len(lat_vec)):    
    plt.cla()
    m = Basemap(projection='ortho', 
              lat_0=lat_vec[pp], lon_0=lon_vec[pp])
    
    # coastlines, map boundary, fill continents/water, fill ocean, draw countries
    m.drawmapboundary(fill_color=ocean_map)
    m.fillcontinents(color=cmap(200),lake_color=ocean_map)
    m.drawcoastlines()
    m.drawcountries()

    #show the plot, introduce a small delay to allow matplotlib to catch up
    plt.show()
    plt.pause(0.01)
    # iterate to create the GIF animation
    gif_maker('basemap_rotating_globe.gif','./png_dir/',gif_indx,len(lat_vec)-1,dpi=90)
    gif_indx+=1

