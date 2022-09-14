# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:20:47 2022

@author: eiaaa001
"""

import os
import subprocess  #Importerer subprocess, som lar deg åpne nye programmer rett fra python.

print("Trykk enter for å åpne Geogebrafiler til PCen krasjer.") #Input field to start the program
input()
 
while True: #Åpner Geogebrafiler til PCen krasjer
    subprocess.Popen(['C:\Program Files (x86)\GeoGebra6.0.723.0\GeoGebra.exe'])