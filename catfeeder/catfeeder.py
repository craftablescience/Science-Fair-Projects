from BrickPi import *
import time, datetime
from flask import Flask, request

pygame.init()
BrickPiSetup()
BrickPi.MotorEnable[PORT_B] = 1
BrickPiSetupSensors()
app = Flask(__name__)

class CatFeeder(object):
    def __init__(self, motorSpeed, motorLength):
        self.motorSpeed = motorSpeed
        self.motorLength = motorLength

    def __str__(self):
        return "Motor Speed: " + str(self.motorSpeed) + "\nMotor Length: " + str(self.motorLength)

    def getMotorSpeed(self):
        return self.motorSpeed

    def setMotorSpeed(self, newMotorSpeed):
        self.motorSpeed = newMotorSpeed
        return self.motorSpeed

    def getMotorLength(self):
        return self.motorLength

    def setMotorLength(self, newMotorLength):
        self.motorLength = newMotorLength
        return self.motorLength

    def dispense(self):
        BrickPi.MotorSpeed[PORT_B] = self.motorSpeed
        ot = time.time()
        count = time.time() - ot
        while (count <= self.motorLength / 4):
            BrickPiUpdateValues()
            count = time.time() - ot
        BrickPi.MotorSpeed[PORT_B] = -self.motorSpeed
        ot = time.time()
        count = time.time() - ot
        while (count <= self.motorLength / 4):
            BrickPiUpdateValues()
            count = time.time() - ot
        ot = time.time()
        count = time.time() - ot
        BrickPi.MotorSpeed[PORT_B] = self.motorSpeed
        while (count <= self.motorLength / 4):
            BrickPiUpdateValues()
            count = time.time() - ot
        ot = time.time()
        count = time.time() - ot
        BrickPi.MotorSpeed[PORT_B] = -self.motorSpeed
        while (count <= self.motorLength / 4):
            BrickPiUpdateValues()
            count = time.time() - ot
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPiUpdateValues()

catfeeder = CatFeeder(255,4.0)

motorSpeed = 255
motorLength = 4.0
dispenseTime = 12

html_index_f = open("index.html", "r")
html_index = html_index_f.read()
html_index_f.close()

@app.route("/", methods=["GET", "POST"])
def index():
	global motorSpeed, motorLength, dispenseTime
	motorSpeed = request.form.get('speed')
	motorLength = request.form.get('length')
	newDispenseTime = request.form.get('time')
	if motorSpeed != None and catfeeder.getMotorSpeed() != motorSpeed:
		catfeeder.setMotorSpeed(motorSpeed)
	if motorLength != None and catfeeder.getMotorLength() != motorLength:
		catfeeder.setMotorLength(motorLength)
	if newDispenseTime != None:
		dispenseTime = newDispenseTime
	
	return html_index
	
@app.route("/dispenseNow", methods=["GET"])
def dispenseNow():
    catfeeder.dispense()
    return "<!DOCTYPE html><html><head><meta http-equiv=\"refresh\" content=\"5;url=/\"></head><body><p>Successfully dispensed! Redirecting in 5 seconds...</p></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
