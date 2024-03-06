# Home Automation System using AWS IoT and Python
This project is a home automation system that simulates sensors and actuators and uses AWS IoT services to control and monitor devices in your home.

![Home automation system](https://th.bing.com/th/id/OIG4.cXqtmauDjkukvzuzItPD?w=400&h=400&c=6&r=0&o=5&pid=ImgGn)

## Prerequisites
- An AWS account
- AWS CLI installed and configured on your local machine. You
- Python 3.x installed in your system.
- The paho-mqtt Python library installed: `pip install paho-mqtt`

## Architecture
1. Virtual devices simulating sensors and actuators
2. AWS IoT Core to handle MQTT communication between devices and the AWS cloud
3. AWS IoT Rules Engine to process and store incoming data and trigger actions
4. AWS IoT Device Defender for device identity and access management
5. AWS IoT Things Graph for visualizing the system

## Project Structure
1. [device_simulator.py](/device_simulator.py): A Python project to simulate sensors and actuators
2. [aws_iot_rules.yaml](/aws_iot_rules.yaml): AWS IoT rules configuration file
3. [aws_device_defender.yaml](/aws_device_defender.yaml): AWS IoT Device Defender configuration file

## Getting Started
1. Set up AWS IoT by creating a new thing, policy, and certificate.
2. Download the necessary files (root CA, public and private keys) for the certificate.
3. Update the MQTT_BROKER variable in [device_simulator.py](/device_simulator.py) with your new AWS IoT endpoint.
4. Install the paho-mqtt library using `pip install paho-mqtt`.
5. Run the script using the following command: python [device_simulator.py](/device_simulator.py)

## Files

### AWS IoT Rules
> The [aws_iot_rules.yaml](/aws_iot_rules.yaml) file defines two rules to store temperature and light level data in a DynamoDB table.

### AWS IoT Device Defender
> The [aws_device_defender.yaml](/aws_device_defender.yaml) file defines a detector and a template for the device, as well as a target for the device. These resources can be implemented using the boto3 library for device identity and access management.

### Device Simulator 
> The script will simulate the sensor and actuator devices. The data will be published to the MQTT topics defined in the script. Additionally, the script will connect to the AWS IoT MQTT broker and subscribe to the necessary topics.

## Acknowledgments
- [AWS IoT Core documentation](https://docs.aws.amazon.com/iot/)
- [AWS IoT Rules Engine documentation](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)
- [AWS IoT Device Defender documentation](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html)
- [paho-mqtt library documentation](https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html)
- [Python documentation](https://docs.python.org/)
