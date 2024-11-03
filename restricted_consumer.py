from kafka import KafkaConsumer
import matplotlib.pyplot as plt
import numpy as np

# Diccionario para almacenar los datos recibidos
data = {
    "temperature": [],
    "humidity": [],
    "wind_direction": []
}

# Mapeo inverso para decodificar la dirección del viento
wind_direction_map = {
    0b000: "N",
    0b001: "NE",
    0b010: "E",
    0b011: "SE",
    0b100: "S",
    0b101: "SO",
    0b110: "O",
    0b111: "NO"
}

consumer = KafkaConsumer(
    '21004',
    bootstrap_servers='164.92.76.15:9092',
    value_deserializer=lambda m: m  # Consumir los datos como bytes
)

def decode(payload):
    """
    Decodificar los 3 bytes recibidos en temperatura, humedad y dirección del viento.
    """
    # Convertir de bytes a un entero de 24 bits
    value = int.from_bytes(payload, 'big')
    
    # Extraer los 3 bits de la dirección del viento
    wind = value & 0b111
    wind_direction = wind_direction_map[wind]
    
    # Extraer los 7 bits de la humedad
    hum = (value >> 3) & 0b1111111
    
    # Extraer los 14 bits de la temperatura
    temp = (value >> 10) & 0b11111111111111
    temperature = (temp / 16383) * 100  # Desnormalizar a rango 0-100
    
    return {"temperature": temperature, "humidity": hum, "wind_direction": wind_direction}

def plot_all_data():
    """
    Graficar los datos de temperatura, humedad y dirección del viento.
    """
    plt.clf()

    # Gráfico de temperatura
    plt.subplot(3, 1, 1)
    plt.plot(data['temperature'], label='Temperatura (°C)', color='tab:red')
    plt.legend()

    # Gráfico de humedad
    plt.subplot(3, 1, 2)
    plt.plot(data['humidity'], label='Humedad (%)', color='tab:blue')
    plt.legend()

    # Gráfico polar para la dirección del viento
    plt.subplot(3, 1, 3, polar=True)
    directions = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SO': 225, 'O': 270, 'NO': 315}
    wind_angles = [directions[direction] for direction in data['wind_direction']]
    wind_angles = [wind_angles[-1]]
    wind_r = [10] * len(wind_angles)

    plt.scatter(np.deg2rad(wind_angles), wind_r, label='Dirección del viento', color='tab:green')
    plt.ylim(0, 10)
    plt.legend()

    plt.pause(0.1)


plt.ion()

try:
    for message in consumer:
        print(f"Data received: {message.value}")

        decoded_data = decode(message.value)

        print(f"Decoded data: {decoded_data}")

        data["temperature"].append(decoded_data["temperature"])
        data["humidity"].append(decoded_data["humidity"])
        data["wind_direction"].append(decoded_data["wind_direction"])
        
        plot_all_data()

except KeyboardInterrupt:
    plt.show()