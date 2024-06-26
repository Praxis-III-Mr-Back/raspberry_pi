import RPi.GPIO as GPIO
import time
import math

class Servo:
    def __init__(self, servo_pin, offset=0):
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)  # 50 Hz (20ms PWM period)
        self.pwm.start(0)
        self.offset = offset

    def set_servo_angle(self, angle):
        angle_deg = math.degrees(angle+self.offset)
        if angle_deg > 180:
            angle_deg = 180
        if angle_deg < 0:
            angle_deg = 0
        duty_cycle = angle_deg / 18.0 + 2
        self.pwm.ChangeDutyCycle(duty_cycle)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        servo_pin = 17  # Change this to your GPIO pin number
        my_servo = Servo(servo_pin)

        while True:
            angle = float(input("Enter angle (0 to 180): "))
            my_servo.set_servo_angle(angle)

    except KeyboardInterrupt:
        print("\nExiting program")
    finally:
        my_servo.cleanup()
