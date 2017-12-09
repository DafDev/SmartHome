import RPi.GPIO as GPIO
import time

led = 18
movementSensorAtDoor = 17
movementSensorInsideRoom = 27
switchLights = 22
personsInsideRoom = 0
isLightUp = False
stepInOutTime = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(movementSensorAtDoor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(movementSensorInsideRoom, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchLights, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#function which detects when somene enters the room end switch on
#the lights, it also increases the room occupants counter
# return: nomber of room occupants, lights states (swhitched off or on)
def entryPersons():
    global personsInsideRoom
    global isLightUp
    if GPIO.input(movementSensorAtDoor):
        time.sleep(stepInOutTime)
        if GPIO.input(movementSensorInsideRoom):
            isLightUp = True
            personsInsideRoom = personsInsideRoom + 1
            GPIO.output(led, isLightUp)
            print("Someone entered the room")
            print("Number of people inside: " + str(personsInsideRoom))
            time.sleep(stepInOutTime)
            return personsInsideRoom, isLightUp

#function which detects when somene exits the room end switch off
#the lights it it was the last occupant, it also decreases
#the room occupants counter
# return: nomber of room occupants, lights states (swhitched off or on)
def exitPersons():
    global personsInsideRoom
    global isLightUp
    if GPIO.input(movementSensorInsideRoomr) and personsInsideRoom == 1:
        time.sleep(stepInOutTime)
        if GPIO.input(movementSensorAtDoor):
            isLightUp = False
            personsInsideRoom = personsInsideRoom - 1
            GPIO.output(led, isLightUp)
            print("Someone exited the room")
            print("Number of people inside: " + str(personsInsideRoom))
            time.sleep(stepInOutTime)
            return personsInsideRoom, isLightUp
    else:
        if personsInsideRoom > 1:
            personsInsideRoom = personsInsideRoom - 1
            return personsInsideRoom, isLightUp

#swich lights function
def switchLightsFunction():
    global isLightUp
    if GPIO.input(switchLights) == False:
        isLightUp = not isLightUp
    GPIO.output(led, isLightUp)
    return isLightUp

#main loop
GPIO.output(led, False)
try:
    while True:
        entryPersons()
except KeyboardInterrupt():
    GPIO.cleanup()
