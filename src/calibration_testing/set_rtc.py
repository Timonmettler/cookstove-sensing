import urtc
import machine
import utime
import time

i2c = machine.I2C(id = 0,
                  scl = machine.Pin(5),
                  sda = machine.Pin(4))
rtc = urtc.PCF8523(i2c)

datetime = urtc.datetime_tuple(year = time.localtime()[0],
                               month = time.localtime()[1],
                               day=time.localtime()[2],
                               weekday = time.localtime()[6],
                               hour = time.localtime()[3],
                               minute = time.localtime()[4],
                               second = time.localtime()[5])                       
rtc.datetime(datetime)


def get_time():
    datetime = rtc.datetime()
    return datetime.year, datetime.month, datetime.day, datetime.hour, datetime.minute, datetime.second, datetime.weekday, 335


def set_system_rtc():
    datetime = rtc.datetime()
    system_rtc = machine.RTC()
    system_rtc.datetime((
        datetime.year, datetime.month, datetime.day, 
        datetime.weekday, datetime.hour, datetime.minute, datetime.second, 0
    ))


def main():
    set_system_rtc()

    print(utime.time())
    print(time.localtime())
    print(get_time())


if __name__ == "__main__":
    main()
