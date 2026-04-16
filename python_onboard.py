import machine
import time

# Most Nucleo boards use pin "PA5" for the onboard LED
# Other boards might use "PC13" (e.g., Black Pill)
led = machine.Pin("PA5", machine.Pin.OUT) 

print("Starting STM32 Test...")

while True:
    led.value(1)     # Turn LED on
    time.sleep(0.5)  # Wait 500ms
    led.value(0)     # Turn LED off
    time.sleep(0.5)
