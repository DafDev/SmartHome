import os
import glob
import time
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

NUMTEMP = 0
heating = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(heating, GPIO.OUT)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

#Function to achieve the desired temperature
def achieveDesiredTemperature(numtemp):
    while True:
        if read_temp() > f_numtemp:
            GPIO.output(heating,False)
            print("Current temperature: "+str(read_temp())+"C. Desired temperature: "+str(numtemp)+"C")
            print("Goal achieved")
        else:
            GPIO.output(heating,True)
            print("Current temperature: "+str(read_temp())+"C Desired temperature: "+str(numtemp)+"C")


        time.sleep(2)
        return numtemp

def manageDesiredTemperature(numtemp,newvalue=False):
    while newvalue == False:
        achieveDesiredTemperature(numtemp)
    return numtemp

NUMTEMP = input("Type your desired temperature for the room: ")
f_NUMTEMP=float(NUMTEMP)
try:
    while True:
        manageDesiredTemperature(f_NUMTEMP)
except KeyboardInterrupt:
    GPIO.cleanup()
