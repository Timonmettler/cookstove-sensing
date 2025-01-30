import machine
from hx711 import *

print("calibration started")
tare_value = -33476.7
calibration_factor = 2.508349e-05
hx = hx711(machine.Pin(6), machine.Pin(7))
hx.set_power(hx711.power.pwr_up)
hx.set_gain(hx711.gain.gain_128)
hx711.wait_settle(hx711.rate.rate_10)
estimator = 0


def calibrate():
    global tare_value, calibration_factor, estimator
    print("place the scale in its unloaded state.")
    
    while input("press Enter to continue...") != "":
        print("just press Enter when you're ready (don't type anything)!")
    
    
    for i in range (10): # to clear hx values
        hx.get_value()
    
    for i in range (10): # get values
        estimator = estimator + hx.get_value()

    tare_value = estimator / 10
    
    print(f"tare value: {tare_value}")
    
    print(f"place a known weight on the scale.")
    time.sleep(2)
    weight = float(input("type in the weight"))
    
    for i in range (10): # to clear hx values
        hx.get_value()
    
    estimator = 0
    
    for i in range (10): #get values
        estimator = estimator + hx.get_value()
    
    raw_value_with_weight = estimator / 10
    print(f"raw value with weight: {raw_value_with_weight}")
    
    # Calculate calibration factor
    calibration_factor = weight / (raw_value_with_weight - tare_value)
    print(f"calibration factor: {calibration_factor}")


def main():
    calibrate()

    while True:
        for i in range (5):
            hx.get_value()
        weight = (hx.get_value() - tare_value) * calibration_factor
        
        print(weight)
        time.sleep(2)


if __name__ == "__main__":
    main()
