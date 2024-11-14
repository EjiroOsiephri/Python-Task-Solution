import schedule
import time
import socket
from datetime import datetime


def getCurrentTime():
    print("Current Time:", datetime.now())

def getNetworkConnectivity():
    try:
        socket.create_connection(("8.8.8.8", 53))  # test google dns connectivity

        print("Network is connected")
    except OSError:
        print("Network is disconnected: No found network.")

schedule.every(30).seconds.do(getCurrentTime)
schedule.every(30).seconds.do(getNetworkConnectivity)


while True:
    schedule.run_pending()
    time.sleep(1)