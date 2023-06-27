import time
import random
import requests
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ""
AIO_USERNAME = "Baro"
AIO_KEY = "key"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

global_equation ="bao"#global variablex`
def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
    if(feed_id =="equation"):
        global_equation=payload
        print(global_equation)

def init_global_equation():
    global global_equation
    headers = {}
    aio_url ="https://io.adafruit.com/api/v2/Baro/feeds/equation"
    x = requests.get(url=aio_url,headers=headers,verify=False)
    data =x.json()
    global_equation = data["last_value"]
    print("get lastest value:" ,global_equation)

def modify_value(x1,x2,x3):
    global global_equation
    result = eval(global_equation)
    return result

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
init_global_equation()

while True:
    time.sleep(5)
    s1 = random.randint(20, 70)
    s2 = random.randint(0, 100)
    s3 = random.randint(0, 1000)
    client.publish("sensor1", s1)
    client.publish("sensor2", s2)
    client.publish("sensor3", s3)
    s4 = modify_value(s1, s2, s3)
    print(s4)
    pass
