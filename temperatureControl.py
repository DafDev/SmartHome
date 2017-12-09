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
            print("temperature actuelle: "+str(read_temp())+"C")
        else:
            GPIO.output(heating,True)
            print("temperature actuelle: "+str(read_temp())+"C")

        print("Temperature atteinte")
        time.sleep(2)
        return numtemp
def keepDesiredTemperature(numtemp):
    MIN_NUMTEMP=f_numtemp - 0.5
    while True:
        if read_temp() > MIN_NUMTEMP :
            GPIO.output(heating,False)
            print("temperature actuelle: "+str(read_temp())+"C")
        else:
            GPIO.output(heating,True)
            print("temperature actuelle: "+str(read_temp())+"C")
            print("Temperature atteinte")
            time.sleep(2)

def manageDesiredTemperature(numtemp,newvalue=False):
    achieveDesiredTemperature(numtemp)
    while newvalue == False:
        keepDesiredTemperature(numtemp)
    return numtemp

NUMTEMP = input("Entrez une temperature: ")
f_NUMTEMP=float(NUMTEMP)
try:
    while True:
        manageDesiredTemperature(f_NUMTEMP)
except KeyboardInterrupt:
    GPIO.cleanup()
