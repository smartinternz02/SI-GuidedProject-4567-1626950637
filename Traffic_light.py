import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "mawtlg",
        "typeId": "VIT-IOT-device",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()


while True:
    def peolpe_waiting():
        peoplewaiting=random.randint(0,30)
        myData={'People waiting at zebra crossing':peoplewaiting}
        print("Published data Successfully: ", myData)
        return peoplewaiting
    stop_light = peolpe_waiting()
    if stop_light == 30:
        print('Red light')
        time.sleep(2)
    elif stop_light >= 1 and stop_light < 10:
        print('Green light')
        stop_light += 1
        time.sleep(2)
    elif stop_light < 20:
        print('Yellow light')
        stop_light += 1
        time.sleep(2)
    elif stop_light < 30:
        print("Red light")
        stop_light += 1
        time.sleep(2)
    else:
        stop_light = 0
        time.sleep(2)
