import time
import iot_connect
from gopigo import *
from iot_topics import *


servo_range = range(2, 12)


def callbackMove(client, userdata, message):
    print("Topic: ") + message.topic
    print("Message: ") + message.payload
    cmd = message.payload
    if cmd == "w":
        fwd()    # Move forward
    elif cmd == "a":
        left()    # Turn left
    elif cmd == "d":
        right()    # Turn Right
    elif cmd == "x":
        bwd()    # Move back
    elif cmd == "s":
        stop()    # Stop
    elif cmd == "g":
        increase_speed()    # Increase speed
    elif cmd == "f":
        decrease_speed()    # Decrease speed
    elif cmd == "k":
        enable_servo()
        servo(10)
        time.sleep(1)
        servo(150)
        time.sleep(1)
        servo(90)
        disable_servo()
    elif cmd.isdigit():
        if int(cmd) in servo_range:
            enable_servo()
            servo(int(cmd)*14)
            time.sleep(1)
            disable_servo()
    else:
        print("Wrong Command, Please Enter Again")
    time.sleep(1)
    stop()

enable_servo()

# Connect to IoT Gateway and subscribe to topics
client = iot_connect.connectIot()
if client:
    print("successfully connected to AWS IoT")

client.subscribe(topicMove, 1, callbackMove)

while True:
    time.sleep(10)

client.unsubscribe(topicMove)
iot_connect.disconnectIot(client)

disable_servo()
