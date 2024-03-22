from kinematics import Kinematics
from servo import Servo
from camera import Camera
from vision import Vision
import math
import time

kin = Kinematics(5)
joint_servo = Servo(17)
camera = Camera()
vision = Vision()

while True:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    q1, q2 = kin.get_angles(x, y)
    print(math.degrees(q1), math.degrees(q2))
    joint_servo.set_servo_angle(q1)
    time.sleep(0.5)
    joint_servo.set_servo_angle(q2)
    time.sleep(0.5)
    joint_servo.set_servo_angle(0)
    time.sleep(0.5)