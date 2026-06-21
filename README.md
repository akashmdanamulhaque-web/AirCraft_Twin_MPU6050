# AirCraft Twin MPU6050

A real-time aircraft attitude visualization system using an MPU6050 sensor, ESP32, Python, and Panda3D.


# Project Overview

This project creates a digital twin of an aircraft using an MPU6050 IMU sensor. The orientation of the physical sensor is transmitted through an ESP32 and visualized in real time using a 3D aircraft model.

## System Architecture

MPU6050 → ESP32 → Serial Communication → Python → Panda3D → 3D Aircraft Visualization

# Features

* Real-time Roll, Pitch, and Yaw tracking
* 3D aircraft visualization
* Digital Twin concept implementation
* ESP32 serial communication
* Panda3D rendering engine

# Hardware Requirements

* ESP32 DevKit V1
* MPU6050 IMU Sensor
* USB Cable
* Windows PC

# Software Requirements

* Python 3.10+
* Arduino IDE
* Panda3D
* PySerial

Install required Python packages:

```bash
pip install panda3d pyserial
```

# Wiring

## MPU6050 → ESP32

| MPU6050 | ESP32  |
| ------- | ------ |
| VCC     | 3.3V   |
| GND     | GND    |
| SDA     | GPIO21 |
| SCL     | GPIO22 |

# Step 1: Upload ESP32 Code

1. Connect ESP32 to your computer.
2. Open Arduino IDE.
3. Select:

Tools → Board → ESP32 Dev Module

4. Select the correct COM Port.
5. Upload the MPU6050 firmware.

After uploading, verify that Serial Monitor shows Roll, Pitch, and Yaw values.

Example:

```text
1.2,-3.4,15.2
1.1,-3.5,15.1
1.3,-3.4,15.3
```

---

# Step 2: Clone or Download Repository

Download this repository:

```bash
git clone https://github.com/YOUR_USERNAME/AirCraft_Twin_MPU6050.git
```

Or download as ZIP.

# Step 3: Place Aircraft Model

Make sure the aircraft model file is present:

```text
Jet.glb
```

inside the project folder.

# Step 4: Install Dependencies

Open terminal inside the project folder:

```bash
pip install panda3d pyserial
```

# Step 5: Configure COM Port

Open:

```python
mpu_board.py
```

Locate:

```python
serial.Serial("COM11",115200)
```

Change COM11 to your ESP32 COM port if necessary.

Example:

```python
serial.Serial("COM5",115200)
```
# Step 6: Run Visualization

Run:

```bash
python mpu_board.py
```

---

# Expected Behavior

* Keep MPU6050 flat → Aircraft remains level
* Tilt left → Aircraft rolls left
* Tilt right → Aircraft rolls right
* Pitch forward → Aircraft nose points down
* Pitch backward → Aircraft nose points up

---

# Troubleshooting

## COM Port Error

Close:

* Arduino Serial Monitor
* Arduino Serial Plotter

Only one application can use the COM port at a time.

## Aircraft Not Moving

Check:

* ESP32 is connected
* Correct COM port selected
* Serial data is being transmitted

## Aircraft Appears Too Large

Adjust:

```python
self.aircraft.setScale(...)
```

## Aircraft Appears Too Close

Adjust:

```python
self.camera.setPos(...)
```

# Future Improvements

* Low Pass Filter
* Complementary Filter
* Kalman Filter
* Artificial Horizon
* Flight HUD
* ROS2 Integration
* Drone Visualization
* Telemetry Dashboard

# Author

Anamul Akash

