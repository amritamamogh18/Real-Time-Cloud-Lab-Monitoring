# lab_sensor.py
import random
import time
import json
import paho.mqtt.client as mqtt  # Install: pip install paho-mqtt

# AWS IoT Core Settings
AWS_IOT_ENDPOINT = "your-iot-endpoint.iot.region.amazonaws.com"
TOPIC = "university/lab1/monitoring"

def simulate_sensor_data():
    return {
        "lab_id": "lab1",
        "cpu_usage": random.randint(0, 100),  # Random CPU %
        "ram_usage": random.randint(0, 100),  # Random RAM %
        "occupancy": random.choice([True, False])  # Random occupancy
    }

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT Core!")

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set()  # Configure certificates (download from AWS IoT Core)
client.connect(AWS_IOT_ENDPOINT, 8883)

while True:
    data = simulate_sensor_data()
    client.publish(TOPIC, json.dumps(data))
    print("Published:", data)
    time.sleep(10)  # Send data every 10 seconds
