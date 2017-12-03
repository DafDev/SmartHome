import GPIO.out as GPIO

led = 4
movementSensorAtDoor = 17
movementSensorInsideRoom = 27
personsInsideRoom = 0

GPIO.setup(led,GPIO.INPUT)
GPIO.setup(movementSensorAtDoor, GPIO.OUTPUT)
GPIO.setup(movementSensorInsideRoom GPIO.OUTPUT)

def entryPersons(){
    if (movementSensorAtDoor) then:
        if (movementSensorInsideRoom):
            led.High
            personsInsideRoom++
}
