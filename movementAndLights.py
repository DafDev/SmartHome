import GPIO.out as GPIO
import time

led = 4
movementSensorAtDoor = 17
movementSensorInsideRoom = 27
switchLights = 22
personsInsideRoom = 0
isLightUp = False
stepInOutTime = 0.5

GPIO.setup(led,GPIO.OUT)
GPIO.setup(movementSensorAtDoor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(movementSensorInsideRoom, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchLights, GPIO.IN, pull_up_up=GPIO.PUD_UP)


def entryPersons():
    global personsInsideRoom
    global isLightUp
    if GPIO.input(movementSensorAtDoor):
        time.sleep(stepInOutTime)
        if GPIO.input(movementSensorInsideRoom):
            isLightUp = True
            personsInsideRoom = personsInsideRoom + 1
            GPIO.output(led, isLightUp)
            print("Number of people inside: " + str(personsInsideRoom))
            return personsInsideRoom, isLightUp

def exitPersons():
    global personsInsideRoom
    global isLightUp
    if GPIO.input(movementSensorInsideRoomr) and personsInsideRoom == 1:
        time.sleep(stepInOutTime)
        if GPIO.input(movementSensorAtDoor):
            isLightUp = True
            personsInsideRoom = personsInsideRoom - 1
            GPIO.output(led, isLightUp)
            print("Number of people inside: " + str(personsInsideRoom))
            return personsInsideRoom, isLightUp
    else:
        if personsInsideRoom > 1:
            personsInsideRoom = personsInsideRoom - 1    

GPIO.output(led, False)
try:
    while true:
        entryPersons()
except KeyboardInterrupt():
    GPIO.cleanup()
