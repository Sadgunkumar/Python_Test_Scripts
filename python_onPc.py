import serial

# Update 'COM7' (Windows) or '/dev/ttyACM0' (Linux/Mac) to match your board's port
SERIAL_PORT = "COM7" 
BAUD_RATE = 115200

try:
    # Open the serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT}. Waiting for data...")

    while True:
        # Read a line from the STM32 board
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"STM32 Output: {line}")

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nTest stopped by user.")
finally:
    if 'ser' in locals():
        ser.close()
