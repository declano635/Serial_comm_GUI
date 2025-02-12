# Serial_comm_GUI
This project simulates a **hardware device communicating over a UART (serial) connection**, verifies received data, and checks for expected responses.

## 📌 Overview
This project extends the **UART-based verification system** by adding a **GUI serial monitor** that allows users to:
- **View incoming serial data in real-time**.
- **Send test commands** to the simulated hardware.
- **Log and save serial data** for debugging.

## Step 1: Install Required Python Libraries

Before you begin, install the required Python libraries to simulate serial communication and manage configuration files easily.

Run the following command in your terminal:

pip install pyserial pyyaml

Libraries Used:

pyserial: A Python library to simulate serial communication.

pyyaml: A library to handle test configurations in a YAML format, making it easier to edit and manage.

## Step 2: Set Up a Virtual Serial Port on macOS

Since we are simulating hardware, we will create a pair of virtual serial ports using socat. This will allow two Python scripts to communicate as if they were connected to actual hardware.


1️⃣ Install socat

Install socat on macOS using Homebrew:

brew install socat


2️⃣ Create Virtual Serial Ports

After installing socat, run the following command in your terminal to create two virtual serial ports:

socat -d -d pty,raw,echo=0 pty,raw,echo=0

This command will generate two virtual serial ports. The output will look similar to this:

2024/02/10 12:34:56 socat[12345] N PTY is /dev/ttys004

2024/02/10 12:34:56 socat[12345] N PTY is /dev/ttys005


3️⃣ Take Note of the Virtual Ports

Take note of the two virtual serial devices created by socat (e.g., /dev/ttys004 and /dev/ttys005).

One port will be used by the mock hardware script.
The other port will be used by the test script to simulate communication.

## 🚀 Running the Project

1️⃣ Start the Mock Hardware
python mock_hardware.py
(Simulates a device sending test data every 2 seconds.)

2️⃣ Start the GUI Serial Monitor
python serial_gui.py
Click "Connect" to start reading data.
Use the input field to send test messages.
Click "Save Log" to save received data.

3️⃣ (Optional) Run the Test Runner
python test_runner.py
Listens for incoming serial data and verifies expected responses.

🎨 GUI Features

✅ Real-time serial data display

✅ Send test commands via GUI

✅ Save logs for debugging

✅ Automatic detection of available serial ports
