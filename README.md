# IoT Node-Based Security System with ESP32

This project implements a comprehensive security system using IoT nodes with ESP32. The system consists of three main parts: the master node, the slave node, and a mobile application.

## Project Folders

- `Main_master`: Contains the code for the first ESP32 of the master node, responsible for communication with the application and control of devices such as the RFID module and the 4x4 keypad.
- `Main_speaker`: Contains the code for the second ESP32 of the master node, responsible for communication with the slave node and activation of the DFPlayer Mini module for the alarm speaker.
- `Main_slave`: Contains the code for the slave node, which detects motion and door openings, sending alerts to the master node.
- `app`: Contains the code for the mobile application developed in Python with Tkinter and CustomTkinter libraries, which communicates with the master node via MQTT requests to manage the alarm state and display relevant information.

## Key Features

- **Intruder Detection**: The slave node detects motion or door openings and sends alerts to the master node.
- **Alarm Activation and Deactivation**: The user can activate or deactivate the alarm locally using a 4x4 keypad or via the mobile application.
- **Wireless Communication**: The system communicates via WiFi, both between nodes and with the mobile application, using MQTT requests.
- **Energy Saving**: A Deep Sleep mode is implemented in the slave node to reduce energy consumption, waking up via external interruptions.
- **Graphical Interface in the Application**: The mobile application provides an intuitive graphical interface for managing the alarm state and displaying relevant information.
