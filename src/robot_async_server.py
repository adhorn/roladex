from __future__ import print_function
from __future__ import division
import logging
import os.path
import signal
import threading
import robot_controller
import time

LOG_FILENAME = "/tmp/robot_web_server_log.txt"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
# Also log to stdout
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
logging.getLogger("").addHandler(consoleHandler)

try:
    import Queue as queue
except:
    import queue
robot = None

scriptPath = os.path.dirname(__file__)
robotConnectionResultQueue = queue.Queue()
isClosing = False


def createRobot(resultQueue):
    r = robot_controller.RobotController()
    resultQueue.put(r)


Class IoTConnectionHandler():
    def on_message(self, message):
        pass

    def on_close(self):
        logging.info('IoT connection closed')


def robotUpdate():

    global robot
    global isClosing

    if isClosing:
        # clean things up
        return

    if robot is None:
        if not robotConnectionResultQueue.empty():
            robot = robotConnectionResultQueue.get()

    else:

        robot.update()


def signalHandler(signum, frame):

    if signum in [signal.SIGINT, signal.SIGTERM]:
        global isClosing
        isClosing = True


if __name__ == "__main__":

    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)

    # Start connecting to the robot asyncronously
    robotConnectionThread = threading.Thread(
        target=createRobot,
        args=[robotConnectionResultQueue]
    )
    # args=[ robotConfig, robotConnectionResultQueue ] )
    robotConnectionThread.start()
    # Shut down code
    robotConnectionThread.join()

    if robot is not None:
        robot.disconnect()
    else:
        if not robotConnectionResultQueue.empty():
            robot = robotConnectionResultQueue.get()
            robot.disconnect()
