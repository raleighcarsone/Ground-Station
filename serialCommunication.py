# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:38:01 2023

@author: 15129
"""

import serial


#x is asythemyth, y is elevation
def recive(x,y):
    ser = serial.Serial('COM4', 9600)    
    # wait for and read 4-byte hex code from Arduino
    code_bytes = ser.read(4)
    hex_code = hex(int.from_bytes(code_bytes, byteorder='big'))

    # wait for and read 4-byte hex value from Arduino
    hex_value_bytes = ser.read(4)
    hex_value = hex(int.from_bytes(hex_value_bytes, byteorder='big'))

    # close serial connection
    ser.close()

    # return hex code and hex value as tuple
    return hex_code, hex_value
   

    # close serial connection
    ser.close()
    
#x is asythemyth, y is elevation
def sendAngle(x,y,code,code1):
    ser = serial.Serial('COM4', 9600)    
    x1=hex(x)
    y1=hex(y)

    # convert hex code string to bytes
    x_bytes = bytes.fromhex(x1)+code
    y_bytes = bytes.fromhex(y1)+code1
    # write hex bytes to serial port
    ser.write(x_bytes)
    ser.write(y_bytes)
    ser.close()

def reciveDone(done):
   ser = serial.Serial('COM4', 9600)    
   y= ser.read()
   if y==done:
       sendAngle(x, y, code, code1)