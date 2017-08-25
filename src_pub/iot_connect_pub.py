from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from iot_config_pub import *


def connectIot():
    print("connecting to AWS IoT")
    IoTMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
    IoTMQTTClient.configureEndpoint(IOT_ENDPOINT, IOT_PORT)
    IoTMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)
    IoTMQTTClient.connect()
    return IoTMQTTClient


def disconnectIot(IoTMQTTClient):
    print("discconnecting from AWS IoT")
    IoTMQTTClient.disconnect()
