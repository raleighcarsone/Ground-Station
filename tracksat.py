# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:36:07 2023
This script loads a TLE file from Celestrak, which provides orbital data for many satellites. You will need to replace the satellite_name variable with the name of the satellite you want to track, and you may need to adjust the URL of the TLE file if you want to track a satellite that is not included in the default file.

The script then defines the location of the ground station using latitude, longitude, and elevation, and gets the current time using the skyfield library's timescale object.

Finally, the script calculates the satellite's position relative to the ground station using the difference object, which calculates the vector between the satellite and the ground station at the given time. The topocentric object then converts this vector to a topocentric coordinate system (i.e. relative to the ground station). The script prints the altitude and azimuth of the satellite at the given time.

To track the satellite over time, you can put this code in a loop that updates the time and recalculates the satellite's position at regular intervals. You can also use this script as a starting point to build a more sophisticated tracking system that controls a motorized antenna to keep the satellite in view.

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
  
