# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:36:07 2023
This script loads a TLE file from Celestrak, which provides orbital data for many satellites.
@author: 15129
"""


from skyfield.api import load, Topos
import time 
import serialCommunication as sercom

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
        latitude = 29.18368  # in degrees
        longitude = -81.043233  # in degrees
        altitude1 = -12  # in meters
        ground_station = Topos(latitude, longitude, altitude1)
        
        # Get current time
        timeScale = load.timescale()
        currentTime = timeScale.now()
        
        # Calculate satellite's position relative to ground station
        difference = satellite - ground_station
        topocentric = difference.at(currentTime)
        elevation, azimuth = topocentric.altaz()
        
        # Print results and send to the ground station 
        print('Satellite elevation:', elevation)
        print('Satellite azimuth:', azimuth)
        currentLocation=sercom.recieve(elevation,azimuth)
        nextLocation=sercom.sendAngle(elevation , azimuth)
        while (currentLocation != nextLocation):
           currentLocation=sercom.recieve(elevation,azimuth)
        time.sleep(1)
