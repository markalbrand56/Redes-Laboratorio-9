# Estación Meteorológica - lab 9

## 🌐 Tecnologías Utilizadas
- **Python**: para simular los sensores y desarrollar los consumidores Kafka.
- **Apache Kafka**: utilizado como el broker de mensajería para conectar los productores de datos con los consumidores.
- **Matplotlib**: para graficar los datos recolectados y permitir una visualización clara de los parámetros medidos.

## 🔗 Descripción General
En este proyecto, simulamos una estación meteorológica con tres sensores principales:
- **Sensor de Temperatura** (⚡): mide entre 0 y 110 °C con dos decimales de precisión.
- **Sensor de Humedad Relativa** (☔️): mide la humedad como un valor entero entre 0 y 100%.
- **Sensor de Dirección del Viento** (🌬️): indica dirección cardinal ({N, NE, E, SE, S, SO, O, NO}).

### Instalación de Dependencias
```bash
pip install kafka-python matplotlib
```
