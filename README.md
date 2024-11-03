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

### Estrategia de codificación

Se realizaron dos versiones de la pareja de Sensores y Consumidores, una que se comunica con Kafka mediante el uso de `JSON` y otra que se comunica con Kafka simulando una red restrictiva de datos, con un máximo de 3 bytes por mensaje.

En este escenario de la red restrictiva, los mensajes se codifican en un formato binario, donde cada sensor tiene un identificador único y un valor asociado. Para el caso de la dirección del viento, se utilizó un diccionario para mapear las direcciones cardinales a un valor numérico. A continuación se describe la codificación de los mensajes:

- **Sensor de Temperatura**:
  - 14 bits
  - Se codifica el valor de la temperatura en un rango de 0 a 110 °C con dos decimales de precisión. Para utilizar los 14 bits, se utiliza un proceso de normalización del valor de la temperatura, dividiendo el valor real por 110 y multiplicándolo por 2^14. De esta manera se mantiene la precisión de dos decimales.
- **Sensor de Humedad Relativa**:
  - 7 bits
  - Se codifica el valor de la humedad relativa en un rango de 0 a 100%. Al tener 7 bits disponibles, se tiene un máximo de 128 valores posibles, por lo que se decidió mandar el valor de la humedad como un número entero, perdiendo la precisión de los decimales.
- **Sensor de Dirección del Viento**:
  - 3 bits
  - Se codifica la dirección del viento en un rango de 0 a 7, donde cada número representa una dirección cardinal. Para esto, se utilizó un diccionario que mapea las direcciones cardinales a un valor numérico.  

## Cómo Ejecutar

### Requisitos

- **Python 3.8** o superior.
- **Apache Kafka** instalado y corriendo en el puerto 9092. En este laboratorio se proporcionó el servidor de Kafka para todos los estudiantes.

### Instalación de Dependencias

```bash
pip install kafka-python matplotlib
```
