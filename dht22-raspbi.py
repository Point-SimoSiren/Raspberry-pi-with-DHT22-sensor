'''
First give commands in the terminal to update and install the library:
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
'''

import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        
    else:
        print("Failed to retrieve data from humidity sensor")
       
 # This code is from https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
 
 # Im soon going to reform it to be able to send data to backend rest api
