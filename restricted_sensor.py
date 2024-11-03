import random
import time
from models import Data
from kafka import KafkaProducer
import struct

INTERVAL = 5

# Mapeo de direcciones del viento a valores de 3 bits
wind_direction_map = {
    "N": 0b000,
    "NE": 0b001,
    "E": 0b010,
    "SE": 0b011,
    "S": 0b100,
    "SO": 0b101,
    "O": 0b110,
    "NO": 0b111
}

class Sensor:
    producer = KafkaProducer(
        bootstrap_servers='164.92.76.15:9092',
        value_serializer=lambda v: v  # Kafka envía bytes directamente
    )

    def __init__(self):
        self.data = Data(temperature=0, humidity=0, wind_direction="N")

    def record_temperature(self):
        self.data.temperature = random.uniform(0, 100)
        
    def record_humidity(self):
        self.data.humidity = random.uniform(0, 100)
    
    def wind_direction(self):
        self.data.wind_direction = random.choice(list(wind_direction_map.keys()))

    def encode(self):
        """
        Codificar los valores de temperatura, humedad y dirección del viento en 3 bytes.
        """
        # Normalizar temperatura a un valor de 14 bits (0-100 -> 0-16383)
        temp = int((self.data.temperature / 100) * 16383)  # 14 bits
        hum = int(self.data.humidity)  # 7 bits
        wind = wind_direction_map[self.data.wind_direction]  # 3 bits
        
        # Empaquetar en un entero de 24 bits
        payload = (temp << 10) | (hum << 3) | wind
        
        # Convertir el payload a bytes
        return payload.to_bytes(3, 'big')  # 3 bytes

    def record_data(self):
        while True:
            self.record_temperature()
            self.record_humidity()
            self.wind_direction()
            
            encoded_data = self.encode()

            self.producer.send(topic="21004", value=encoded_data)
            print(f"Data sent (restricted): {self.data} -> Encoded: {encoded_data}\n")
            time.sleep(INTERVAL)      

    def __str__(self):
        return f"Temperature: {self.data.temperature}°C, Humidity: {self.data.humidity}%, Wind Direction: {self.data.wind_direction}"


sensor = Sensor()

print("Starting sensor...")

try:
    sensor.record_data()
except KeyboardInterrupt:
    print("Sensor stopped.")  