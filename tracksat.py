# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:36:07 2023

@author: 15129
"""


from skyfield.api import load, Topos
import time 

altitude = 0
azimuth = 0

def tracking(satname):
    # Load TLE file for satellite
    while True:
        satellite_name = satname
        tle_url = 'https://www.celestrak.com/NORAD/elements/stations.txt'
        satellites = load.tle_file(tle_url)
        satellite = None
        for sat in satellites:
            if sat.name == satellite_name:
                satellite = sat
                break
        if satellite is None:
            raise ValueError('Satellite not found')
        
        # Define location of ground station
        latitude = 40.0  # in degrees
        longitude = -105.0  # in degrees
        elevation = 2000  # in meters
        ground_station = Topos(latitude, longitude, elevation)
        
        # Get current time
        timeScale = load.timescale()
        currentTime = timeScale.now()
        
        # Calculate satellite's position relative to ground station
        difference = satellite - ground_station
        topocentric = difference.at(currentTime)
        altitude, azimuth, distance = topocentric.altaz()
        
        # Print results
        print('Satellite altitude:', altitude)
        print('Satellite azimuth:', azimuth)
        
        time.sleep(1)
  
