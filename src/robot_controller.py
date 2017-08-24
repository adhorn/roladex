from __future__ import print_function
from __future__ import division
import math
import time
import gopigo


debug = 0


class RobotController:

    MAX_UPDATE_TIME_DIFF = 0.25
    TIME_BETWEEN_SERVO_SETTING_UPDATES = 1.0

    JOYSTICK_DEAD_ZONE = 0.1

    MOTION_COMMAND_TIMEOUT = 2.0
    # If no commands for the motors are recieved in this time then
    # the motors (drive and servo) are set to zero speed
    speed_l = 200
    speed_r = 200

    def __init__(self):
        gopigo.set_speed(200)
        gopigo.fwd()
        gopigo.stop()

        self.lastServoSettingsSendTime = 0.0
        self.lastUpdateTime = 0.0
        self.lastMotionCommandTime = time.time()

    def __del__(self):

        self.disconnect()

    def disconnect(self):
        print("__ Closing __")

    def normaliseJoystickData(self, joystickX, joystickY):
        stickVectorLength = math.sqrt(joystickX**2 + joystickY**2)
        if stickVectorLength > 1.0:
            joystickX /= stickVectorLength
            joystickY /= stickVectorLength

        if stickVectorLength < self.JOYSTICK_DEAD_ZONE:
            joystickX = 0.0
            joystickY = 0.0

        return (joystickX, joystickY)

    def centreNeck(self):
        #gopigo.set_right_speed(0)
        pass

    def setMotorJoystickPos(self, joystickX, joystickY):
        joystickX, joystickY = self.normaliseJoystickData(joystickX, joystickY)
        if debug:
            print("Left joy", joystickX, joystickY)
            #print self.speed_l*joystickY
        #gopigo.set_left_speed(int(self.speed_l*joystickY))
        #gopigo.fwd()
        if joystickX > .5:
            print("Left")
            gopigo.left()
        elif joystickX < -.5:
            print("Right")
            gopigo.right()
        elif joystickY > .5:
            print("Fwd")
            gopigo.fwd()
        elif joystickY < -.5:
            print("Back")
            gopigo.bwd()
        else:
            print("Stop")
            gopigo.stop()

    def setNeckJoystickPos(self, joystickX, joystickY):
        #print ("g")
        joystickX, joystickY = self.normaliseJoystickData(joystickX, joystickY)
        if debug:
            print("Right joy", joystickX, joystickY)
            #print (self.speed_r*joystickY)
        #gopigo.set_right_speed(int(self.speed_r*joystickY))
        #gopigo.fwd()
        #self.lastMotionCommandTime = time.time()

    def update(self):
        if debug:
            print("Updating")
        curTime = time.time()
        timeDiff = min(
            curTime - self.lastUpdateTime, self.MAX_UPDATE_TIME_DIFF
        )

        # Turn off the motors if we haven't received a motion command for a while
        #if curTime - self.lastMotionCommandTime > self.MOTION_COMMAND_TIMEOUT:
        #   self.leftMotorSpeed = 0.0
        #   self.rightMotorSpeed = 0.0
        #   self.panSpeed = 0.0
        #   self.tiltSpeed = 0.0

        self.lastUpdateTime = curTime
