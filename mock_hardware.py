import serial
import time

# Serial port for simulated hardware
SERIAL_PORT = "/dev/ttys021"  # Change if using real hardware
BAUD_RATE = 9600

# Open serial connection
ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)
print(f"[Mock Hardware] Sending data to {SERIAL_PORT} at {BAUD_RATE} baud.")

try:
    while True:
        test_data = "Hello from Mock Hardware!\n"
        ser.write(test_data.encode('utf-8'))  # Send data
        print(f"[Mock Hardware] Sent: {test_data.strip()}")
        time.sleep(2)  # Simulate periodic transmission
except KeyboardInterrupt:
    print("[Mock Hardware] Stopped.")
finally:
    ser.close()

