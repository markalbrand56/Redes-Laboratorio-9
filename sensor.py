import random
import json
import time
from models import Data
from kafka import KafkaProducer

INTERVAL = 5

class Sensor:
    producer = KafkaProducer(
        bootstrap_servers='164.92.76.15:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    def __init__(self):
        self.data = Data(temperature=0, humidity=0, wind_direction="N")

    def record_temperature(self):
        self.data.temperature = random.uniform(0,110)
        
    def record_humidity(self):
        self.data.humidity = random.uniform(0,100)
    
    def wind_direction(self):
        self.data.wind_direction = random.choice(["N", "NO", "O", "SO", "S", "SE", "E", "NE"])

    def record_data(self):
        while True:
            self.record_temperature()
            self.record_humidity()
            self.wind_direction()
            
            json_data = json.dumps(self.data.__dict__)

            self.producer.send(topic="21004", value=json_data)
            print(f"Data sent: {self.data}\n")
            time.sleep(INTERVAL)      

    def __str__(self):
        return f"Temperature: {self.data.temperature}°C, Humidity: {self.data.humidity}%, Wind Direction: {self.data.wind_direction}"


sensor = Sensor()

print("Starting sensor...")

try:
    sensor.record_data()
except KeyboardInterrupt:
    print("Sensor stopped.")    
