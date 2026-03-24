# **Medicine Dispenser Project**

A simple, modular **automatic medicine dispenser** built using **ESP32**, **PCA9685 servo driver**, **IR sensors**, and **3D-printed components**. This project allows you to schedule and dispense medicines remotely via a web interface.

---

## **Features**
- Dispenses pills from multiple buckets using servo motors.
- Detects pill drops using IR sensors.
- Web-based control panel (ESP32 provides IP address).
- Modular design – easy to extend or modify.
- Open-source hardware and software.

---

## **Folder Structure**
medicine-dispenser/
│
├── README.md                # Project documentation  
├── LICENSE                  # License file (CC BY-NC 4.0)  
├── hardware/   
│   ├── connection_mapping.png   # Wiring diagram  
│   └── latest_version_2.2/               # STL files for 3D printing  
├── firmware/   
│   └── main.ino         # ESP32 Arduino code   
│   └── test.ino         # ESP32 Arduino code   
└── Media/                  # Extra images/screenshots  


---

## **Hardware Required**
- **ESP32** development board
- **PCA9685 16-channel PWM driver**
- **3x 180° Servo motors** (e.g., SG90 or MG90S)
- **3x IR sensor modules** (active LOW)
- **5V power supply** (≥3A recommended)
- Jumper wires, breadboard or PCB
- **Optional**: Vibration motor for pill alignment
- **3D-printed parts** (download STL files from `hardware/3D-models/`)

---

## **Connection Diagram**
!Connection Diagram

---

## **Wiring Connections**
| **From**                | **To**                     | **Notes** |
|-------------------------|---------------------------|-----------|
| ESP32 **3V3**          | PCA9685 **VCC**          | Logic power |
| ESP32 **GND**          | PCA9685 **GND**          | Common ground |
| ESP32 **GND**          | **5V Supply GND**        | Common ground |
| **5V Supply +**        | PCA9685 **V+**           | Servo power rail |
| ESP32 **GPIO21 (SDA)** | PCA9685 **SDA**          | I²C data |
| ESP32 **GPIO22 (SCL)** | PCA9685 **SCL**          | I²C clock |
| Servo (bucket 0)       | PCA9685 **CH15**         | Matches `servoChannels[0]` |
| Servo (bucket 1)       | PCA9685 **CH14**         | Matches `servoChannels[1]` |
| Servo (bucket 2)       | PCA9685 **CH13**         | Matches `servoChannels[2]` |
| All servo **red**      | PCA9685 **V+**           | 5V |
| All servo **brown/black** | PCA9685 **GND**       | Common ground |
| Sensor 0 **DO**        | ESP32 **GPIO34**         | Active‑LOW |
| Sensor 1 **DO**        | ESP32 **GPIO35**         | Active‑LOW |
| Sensor 2 **DO**        | ESP32 **GPIO32**         | Active‑LOW |
| Sensors **VCC**        | ESP32 **3V3**            | Use 3.3V for logic safety |
| Sensors **GND**        | **GND**                  | Common ground |

---

## **Setup Instructions**
1. **Install Arduino IDE** and ESP32 board support.
2. Install required libraries:
   - `Adafruit PWM Servo Driver`
   - `Wire`
3. Open `firmware/dispenser_v1.ino` in Arduino IDE.
4. Select **ESP32 board** and upload the code.
5. Open Serial Monitor to get the **IP address**.
6. Access the web interface via the IP address to:
   - Schedule dispensing
   - Open/close trays
   - Monitor status

---

## **How It Works**
- Place medicines in the corresponding trays.
- The ESP32 runs a web server for scheduling and manual control.
- Servos rotate to dispense pills; IR sensors confirm pill drops.
- PCA9685 handles servo PWM signals for smooth operation.

---

## **Future Improvements**
- Improve suspension design for better stability.
- Change bucket arrangement (circular, radial, etc.).
- Add vibration motor for consistent pill flow.
- Use a stronger base plate for uniform vibration distribution.
- Add more buckets or integrate with IoT platforms.

---

## **License**
This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.  
You may use, share, and modify this project for **personal and educational purposes**, but **commercial use is prohibited**.  
Read full license

---