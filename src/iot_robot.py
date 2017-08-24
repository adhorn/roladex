import time
import iot_connect
from gopigo import *
from iot_topics import *


def callbackMove(client, userdata, message):
    print "Topic="+message.topic
    print "Message="+message.payload
    cmd = message.payload
    if cmd == "forward":
        fwd()    # Move forward
    elif cmd == "left":
        left()    # Turn left
    elif cmd == "right":
        right()    # Turn Right
    elif cmd == "backward":
        bwd()    # Move back
    elif cmd == "stop":
        stop()    # Stop
    elif cmd == "faster":
        increase_speed()    # Increase speed
    elif cmd == "slower":
        decrease_speed()    # Decrease speed
    else:
        print "Wrong Command, Please Enter Again"
    time.sleep(1)
    stop()


def callbackLive(client, userdata, message):
    print("starting live video feed")


# Connect to IoT Gateway and subscribe to topics
client = iot_connect.connectIot()
if client:
    print("successfully connected to AWS IoT")

client.subscribe(topicMove, 1, callbackMove)

while True:
    time.sleep(10)

client.unsubscribe(topicMove)
iot_connect.disconnectIot(client)
