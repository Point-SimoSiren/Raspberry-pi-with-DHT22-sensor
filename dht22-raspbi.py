'''
First give commands in the terminal to update and install the library:
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
'''
import os
import time
import Adafruit_DHT
import math
import requests

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

print("Starting")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print("Raw humidity: ", humidity)
    print("Raw temperature: ", temperature)
    h = truncate(humidity, 2)
    t = truncate(temperature, 2)
    print("Rounded humidity: ", h)
    print("Rounded temperature: ", t)

    url = 'https://timesheetrest.azurewebsites.net/api/measurements'

    mittaus = {'Sender': 'rpi+DHT22/Simo', 'Temperature': t, 'Humidity': h, 'Pressure': 0 }

    x = requests.post(url, json = mittaus)

    print("Back-end vastasi: ", x.text)

    time.sleep(10)

