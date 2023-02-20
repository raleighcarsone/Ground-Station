# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:38:01 2023

@author: 15129
"""

import serial
ser = serial.Serial('COM4', 9600)
ser.write(0x1)
ser.read_all()