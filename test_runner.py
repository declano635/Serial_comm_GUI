import serial

# Serial port for receiving data
SERIAL_PORT = "/dev/ttys022"  # Change if using real hardware
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)
print(f"[Test Runner] Listening on {SERIAL_PORT} at {BAUD_RATE} baud.")

try:
    while True:
        received_data = ser.readline().decode('utf-8').strip()  # Read incoming data
        if received_data:
            print(f"[Test Runner] Received: {received_data}")

            # Verification logic
            if "Hello" in received_data:
                print("[PASS] Expected message received.")
            else:
                print("[FAIL] Unexpected data received.")

except KeyboardInterrupt:
    print("[Test Runner] Stopped.")
finally:
    ser.close()
