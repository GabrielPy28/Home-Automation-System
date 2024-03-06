import random
import time
import paho.mqtt.client as mqtt

# MQTT settings
MQTT_BROKER = "your-iot-endpoint.com" # Replace 'your-iot-endpoint.com' with your AWS IoT endpoint.
MQTT_PORT = 8883
MQTT_TOPIC_TEMP = "home/temperature"
MQTT_TOPIC_LIGHT = "home/light"

# Device settings
TEMP_MIN = 20
TEMP_MAX = 30
LIGHT_MIN = 0
LIGHT_MAX = 100

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_TEMP + "/set")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = int(msg.payload)
    print("Received message: " + topic + " " + str(payload))
    if topic == MQTT_TOPIC_TEMP + "/set":
        set_temperature(payload)

def set_temperature(value):
    print("Setting temperature to " + str(value))
    time.sleep(1)  # Simulate delay in changing temperature
    current_temp = random.uniform(TEMP_MIN, TEMP_MAX)
    print("Current temperature: " + str(current_temp))
    client.publish(MQTT_TOPIC_TEMP, str(current_temp))

def simulate_light():
    while True:
        light_level = random.uniform(LIGHT_MIN, LIGHT_MAX)
        print("Light level: " + str(light_level))
        client.publish(MQTT_TOPIC_LIGHT, str(light_level))
        time.sleep(5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the MQTT loop
client.loop_start()

# Simulate light level changes
simulate_light()