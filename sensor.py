import random
import json
import time

from models import Data

#from kafka import KafkaProducer
#producer = KafkaProducer(bootstrap_servers='164.92.76.15:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))


class Sensor:

    def __init__(self):
        self.data = Data(temperature=0, humidity=0, wind_direction="N")

    def record_temperature(self):
        self.data.temperature = random.uniform(0,100)
        
    def record_humidity(self):
        self.data.humidity = random.uniform(0,100)
    
    def wind_direction(self):
        self.data.wind_direction = random.choice(["N", "NO", "O", "SO", "S", "SE", "E", "NE"])


    def record_data(self):
        self.record_temperature()
        self.record_humidity()
        self.wind_direction()

    def __str__(self):
        return f"Temperature: {self.data.temperature}°C, Humidity: {self.data.humidity}%, Wind Direction: {self.data.wind_direction}"


sensor = Sensor()

print("Starting sensor...")
sensor.record_data()
print(sensor)
