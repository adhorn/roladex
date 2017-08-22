from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from iot_config import *


def connectIot():
    print("connecting to AWS IoT")
    myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
    myMQTTClient.configureEndpoint(IOT_ENDPOINT, IOT_PORT)
    myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)
    myMQTTClient.connect()
    return myMQTTClient


def disconnectIot(myMQTTClient):
    print("discconnecting from AWS IoT")
    myMQTTClient.disconnect()
