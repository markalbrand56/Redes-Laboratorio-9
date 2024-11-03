from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
import numpy as np

data = {
    "temperature": [],
    "humidity": [],
    "wind_direction": []
}

consumer = KafkaConsumer(
    '21004',
    bootstrap_servers='164.92.76.15:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def plot_all_data():
    plt.clf()  

    plt.subplot(3, 1, 1)
    plt.plot(data['temperature'], label='Temperatura (°C)', color='tab:red')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(data['humidity'], label='Humedad (%)', color='tab:blue')
    plt.legend()

    plt.subplot(3, 1, 3, polar=True)
    directions = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SO': 225, 'O': 270, 'NO': 315}
    wind_angles = [directions[direction] for direction in data['wind_direction']]
    wind_angles = [wind_angles[-1]]
    wind_r = [10] * len(wind_angles)

    plt.scatter(np.deg2rad(wind_angles), wind_r, label='Dirección del viento', color='tab:green')
    plt.ylim(0, 10)
    plt.legend()

    plt.pause(0.1)


plt.ion()  # modo interactivo

try:
    for message in consumer:
        print(f"Data received: {message.value}")

        json_data = json.loads(message.value)

        data["temperature"].append(json_data["temperature"])
        data["humidity"].append(json_data["humidity"])
        data["wind_direction"].append(json_data["wind_direction"])
        
        plot_all_data()

except KeyboardInterrupt:
    plt.show()  
