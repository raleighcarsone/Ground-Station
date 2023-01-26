# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:40:03 2022

@author: 15129
"""
import os

os.environ['PROJ_LIB'] = '/Users/mb/anaconda3/envs/worklab/share/proj' 
import datetime,matplotlib,time
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from gifly import gif_maker

plt.ion()
fig,ax0 = plt.subplots(figsize=(5.3,4))
ax0.set_position([0.0,0.0,1.0,1.0])

lat_viewing_angle = [20,20]
lon_viewing_angle = [180,-180]
rotation_steps = 150
lat_vec = np.linspace(lat_viewing_angle[0],lat_viewing_angle[0],rotation_steps)
lon_vec = np.linspace(lon_viewing_angle[0],lon_viewing_angle[1],rotation_steps)

m1 = Basemap(projection='ortho', 
          lat_0=lat_vec[0], lon_0=lon_vec[0],resolution=None)

# add axis for space background effect
#galaxy_image = plt.imread('galaxy.jpg')
ax0.imshow(Blacks)
ax0.set_axis_off()
ax1 = fig.add_axes([0.25,0.2,0.5,0.5])

# define map coordinates from full-scale globe
map_coords_xy = [m1.llcrnrx,m1.llcrnry,m1.urcrnrx,m1.urcrnry]
map_coords_geo = [m1.llcrnrlat,m1.llcrnrlon,m1.urcrnrlat,m1.urcrnrlon]

#zoom proportion and re-plot map 
zoom_prop = 2.0 # use 1.0 for full-scale map

gif_indx = 0
for pp in range(0,len(lat_vec)):

    ax1.clear()
    ax1.set_axis_off()
    ax1.imshow(galaxy_image)
    m = Basemap(projection='ortho',resolution='l',
              lat_0=lat_vec[pp],lon_0=lon_vec[pp],llcrnrx=-map_coords_xy[2]/zoom_prop,
                llcrnry=-map_coords_xy[3]/zoom_prop,urcrnrx=map_coords_xy[2]/zoom_prop,
                urcrnry=map_coords_xy[3]/zoom_prop)

    m.bluemarble(scale=0.5)
    m.drawcoastlines()
    plt.show()
    plt.pause(0.01)
    gif_maker('blue_marble_rotating_globe.gif','./png_dir_bluemarble/',gif_indx,len(lat_vec)+1,dpi=90)
    gif_indx+=1