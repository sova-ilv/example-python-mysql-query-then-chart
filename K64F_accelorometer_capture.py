###########################################################################
# K64_accelorometer_capture.py
# 1. Python code that receives and parses serial port string data
# 2. Decodes x,y,z accelerometer data from Freescale K64_FRDM Kinetis Board
# 3. Continously Plot and update last 12 readings into charts using mathplotlib
# Accel device = FXO8700CQ
# paired with Firmware (K64_AACCELOROMETER)
# https://developer.mbed.org/compiler/#nav:/K64_ACCELOROMETER
# created by Jess Valdez
############################################################################

import serial
import time
import unicodedata
import string
import re
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


Xstr = '0'
Xnum = 0


fig = plt.figure()
ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,4)
ax5 = fig.add_subplot(3,2,5)
ax6 = fig.add_subplot(3,2,6)



Yxar = [0,1,2,3,4,5,6,7,8,9,10,11]
Yyar = [0,0,0,0,0,0,0,0,0,0,0,0]
Yyar2 = [0,0,0,0,0,0,0,0,0,0,0,0]
Yyar3 = [0,0,0,0,0,0,0,0,0,0,0,0]

Yyar_mean = [0,0,0,0,0,0,0,0,0,0,0,0]

#magnetomer
mYyar = [0,0,0,0,0,0,0,0,0,0,0,0]
mYyar2 = [0,0,0,0,0,0,0,0,0,0,0,0]
mYyar3 = [0,0,0,0,0,0,0,0,0,0,0,0]


########################
#serial port business
#########################
ser = serial.Serial(
    port='COM30',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)


def animate(i):
    line = ser.readlines()
    nline = str(line)
    
    N = nline.find('N:') 
    Nstr = str (nline[(N+3):(N+5)])
    Nstr.strip()
    if len(Nstr) > 0:
        Nnum = int(Nstr)
        print (Nnum)
        
    #print (linenum)
    #############################
    #accellerometer X,Y,Z data
    #############################    
    X = nline.find('X:') 
    Xstr = str (nline[(X+3):(X+8)])
    Xstr.strip()
    if len(Xstr) > 0:
        Xnum = int(Xstr)
        print (Xnum)
        Yyar[Nnum] = Xnum + sum(Yyar[0:11]) / 13.0
        for i in range(len(Yyar)):
                       Yyar[i] = sum(Yyar[0:11]) / 12.0
        ax1.clear()
        ax1.plot(Yxar,Yyar, label = 'accel X', linewidth=3, color='r')
        ax1.set_title('accel X',fontsize=12, color='r')
        #ax1.axvspan(-500, 500, facecolor='g', alpha=0.5)
        ax1.set_ylim([-500,800])
        ax1.set_autoscaley_on(False)
        ax1.autoscale_view()

    Y = nline.find('Y:')   
    Ystr = str (nline[(Y+3):(Y+8)])
    Ystr.strip()
    if len(Ystr) > 0:
        Ynum = int(Ystr)
        print (Ynum)
        Yyar2[Nnum] = Ynum + sum(Yyar2[0:11]) / 13.0
        for i in range(len(Yyar2)):
                       Yyar2[i] = sum(Yyar2[0:11]) / 12.0
        ax2.clear()
        ax2.plot(Yxar,Yyar2, label = 'accel Y', linewidth=3, color='r')
        #legend = ax2.legend(loc='upper center', shadow=True)
        ax2.set_title('accel Y',fontsize=12,color='r')
        ax2.set_ylim([-100,1000])
        ax2.set_autoscaley_on(False)
        ax2.autoscale_view()
        
    Z = nline.find('Z:')    
    Zstr = str (nline[(Z+3):(Z+8)])
    Zstr.strip()
    if len(Zstr) > 0:
        Znum = int(Zstr)
        print (Znum)
        Yyar3[Nnum] = Znum + sum(Yyar3[0:11]) / 13.0
        for i in range(len(Yyar3)):
                       Yyar3[i] = sum(Yyar3[0:11]) / 12.0
        ax3.clear()
        ax3.plot(Yxar,Yyar3, label = 'accel Z', linewidth=3, color='r')
        #legend = ax3.legend(loc='upper center', shadow=True)
        ax3.set_title('accel Z',fontsize=12,color='r')
        ax3.set_ylim([-100,1300])
        ax3.set_autoscaley_on(False)
        ax3.autoscale_view()
    #############################
    #magnetometer X,Y,Z data
    #############################
    mX = nline.find('2X:') 
    mXstr = str (nline[(mX+3):(mX+8)])
    mXstr.strip()
    if len(mXstr) > 0:
        mXnum = int(mXstr)
        print (mXnum)
        mYyar[Nnum] = mXnum + sum(mYyar[0:11]) / 13.0
        for i in range(len(mYyar)):
                       mYyar[i] = sum(mYyar[0:11]) / 12.0
        ax4.clear()
        ax4.plot(Yxar,mYyar, label = 'mag X', linewidth=3, color='b')
        #legend = ax4.legend(loc='upper center', shadow=True)
        #ax4.setp(mYyar, linewidth=2, color='r')
        ax4.set_title('mag X',fontsize=12,color='b')
        ax4.set_ylim([0,500])
        ax4.set_autoscaley_on(False)
        ax4.autoscale_view()
        
    mY = nline.find('2Y:')   
    mYstr = str (nline[(mY+3):(mY+8)])
    mYstr.strip()
    if len(mYstr) > 0:
        mYnum = int(mYstr)
        print (mYnum)
        mYyar2[Nnum] = mYnum + sum(mYyar2[0:11]) / 13.0
        for i in range(len(mYyar2)):
                       mYyar2[i] = sum(mYyar2[0:11]) / 12.0
        ax5.clear()
        ax5.plot(Yxar,mYyar2, label = 'mag Y', linewidth=3, color='b')
        #legend = ax5.legend(loc='upper center', shadow=True)
        ax5.set_title('mag Y',fontsize=12,color='b')
        ax5.set_ylim([-120,100])
        ax5.set_autoscaley_on(False)
        ax5.autoscale_view()
        
    mZ = nline.find('2Z:')    
    mZstr = str (nline[(mZ+3):(mZ+8)])
    mZstr.strip()
    if len(Zstr) > 0:
        mZnum = int(mZstr)
        print (mZnum)
        mYyar3[Nnum] = mZnum + sum(mYyar3[0:11]) / 13.0
        for i in range(len(mYyar3)):
                       mYyar3[i] = sum(mYyar3[0:11]) / 12.0
        ax6.clear()
        ax6.plot(Yxar,mYyar3, label = 'mag Z', linewidth=3, color='b')
        #legend = ax6.legend(loc='upper center', shadow=True)
        ax6.set_title('mag Z',fontsize=12,color='b')
        ax6.set_ylim([0,500])
        ax6.set_autoscaley_on(False)
        ax6.autoscale_view()
        
ani = animation.FuncAnimation(fig, animate, interval=700)

plt.show()

ser.close()



