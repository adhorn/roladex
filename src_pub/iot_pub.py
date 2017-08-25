from pynput import keyboard
import iot_connect_pub
from iot_topics_pub import topicMove

# Connect to IoT Gateway and subscribe to topics
client = iot_connect_pub.connectIot()
if client:
    print("successfully connected to AWS IoT")


def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if key == keyboard.Key.esc:
        return False  # stop listener
    if k in ['w', 'x', 'a', 'd']:  # keys interested
        print('Key pressed: ' + k)
        client.publish(topicMove, k, 1)
        return True

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
