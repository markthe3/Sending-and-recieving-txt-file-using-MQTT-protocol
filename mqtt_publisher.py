import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("TextFile_Publisher")
client.connect(mqttBroker)

file_path = "C:/Users/PC/OneDrive/Bureau/test.txt"  # Specify the path to your text file

with open(file_path, "r") as file:
    text_content = file.read()
    client.publish("TEXT_FILE", text_content)
    print("Text file content published to Topic TEXT_FILE")

client.disconnect()

