import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message on topic: ", message.topic)
    if message.topic == "TEXT_FILE":  # Check if the topic is TEXT_FILE
        received_content = str(message.payload.decode("utf-8"))
        with open("test.txt", "w") as file:
            file.write(received_content)
        print("Text file content saved to 'test.txt'")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEXT_FILE")  # Subscribe to the TEXT_FILE topic
client.on_message = on_message
time.sleep(30)  # Keep the script running for 30 seconds
client.loop_stop()  # Stop the loop after 30 seconds

