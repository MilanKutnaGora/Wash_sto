import RPi.GPIO as GPIO
import time


class CarWashComponents:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.soap_pump_pin = 17
        self.brush_motor_pin = 18
        self.water_pump_pin = 23
        self.dryer_fan_pin = 24

        GPIO.setup(self.soap_pump_pin, GPIO.OUT)
        GPIO.setup(self.brush_motor_pin, GPIO.OUT)
        GPIO.setup(self.water_pump_pin, GPIO.OUT)
        GPIO.setup(self.dryer_fan_pin, GPIO.OUT)

    def activate_soap_pump(self, duration):
        GPIO.output(self.soap_pump_pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.soap_pump_pin, GPIO.LOW)

    def activate_brush_motor(self, duration):
        GPIO.output(self.brush_motor_pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.brush_motor_pin, GPIO.LOW)

    def activate_water_pump(self, duration):
        GPIO.output(self.water_pump_pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.water_pump_pin, GPIO.LOW)

    def activate_dryer_fan(self, duration):
        GPIO.output(self.dryer_fan_pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.dryer_fan_pin, GPIO.LOW)

    def deactivate_all(self):
        GPIO.output(self.soap_pump_pin, GPIO.LOW)
        GPIO.output(self.brush_motor_pin, GPIO.LOW)
        GPIO.output(self.water_pump_pin, GPIO.LOW)
        GPIO.output(self.dryer_fan_pin, GPIO.LOW)