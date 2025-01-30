import machine
import time
 
# Create an ADC object on pin 26 (ADC0), which corresponds to physical pin 32 on the Pico
ad8495 = machine.ADC(26)
 
# Constants for calculations
VREF = 3.3  # Reference voltage for the Pico ADC
ADC_RESOLUTION = 65535  # 16-bit ADC resolution
 
def get_voltage(adc_pin):
    """ convert the ADC reading to voltage """
    return (adc_pin.read_u16() * VREF) / ADC_RESOLUTION
 
temperature_c = (get_voltage(ad8495) - 1.25) / 0.005


def main():
    while True:
        # Calculate the temperature from the AD8495 in Celsius
        temperature_c = (get_voltage(ad8495) - 1.25) / 0.005 * 0.3 + 0.7 * temperature_c
        
        # Print the temperatures and voltage
        print("Temperature: {:.2f} °C".format(temperature_c))
        print("Voltage: {:.2f} V".format(get_voltage(ad8495)))
        
        # Wait for 0.5 seconds before the next reading
        time.sleep(0.5)


if __name__ == "__main__":
    main()
