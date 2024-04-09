from kinematics import Kinematics
from servo import Servo
from camera import Camera
#from vision import Vision
import math
import time

kin = Kinematics(5)
head_servo = Servo(17, 0.7)
joint_servo = Servo(18, -0.6)
base_1 = Servo(14, 0.55)
base_2 = Servo(15, -0.55)
camera = Camera()
# vision = Vision()

# while True:
#     x = float(input("Enter x: "))
#     y = float(input("Enter y: "))
#     q1, q2 = kin.get_angles(x, y)
#     print(math.degrees(q1), math.degrees(q2))
#     joint_servo.set_servo_angle(q1)
#     time.sleep(0.5)
#     joint_servo.set_servo_angle(q2)
#     time.sleep(0.5)
#     joint_servo.set_servo_angle(0)
#     time.sleep(0.5)

def set_base_angle(angle):
    base_1.set_servo_angle(angle)
    base_2.set_servo_angle(math.pi - angle)

def interp(a, b, t):
    return a + (b-a)*t

def scan_down():
    set_base_angle(math.pi/2-0.2)
    joint_servo.set_servo_angle(math.pi/2+0.3)
    head_servo.set_servo_angle(math.pi/2)
    time.sleep(15)

    print("Starting...")
    
    steps = 200
    seconds = 25
    for dbase in range(0, steps):
        db = dbase/steps
        set_base_angle(interp(math.pi/2-0.2, 0, db))
        joint_servo.set_servo_angle(interp(math.pi/2+0.3, math.pi, db))
        head_servo.set_servo_angle(interp(math.pi/2, math.pi, db))
        time.sleep(seconds/steps)

def procedure():
    set_base_angle(0)
    joint_servo.set_servo_angle(0)
    head_servo.set_servo_angle(math.pi)
    time.sleep(5)

    print("Starting...")
    
    steps = 200
    seconds = 15

    for dbase in range(0, steps):
        db = dbase/steps
        set_base_angle(interp(0, math.pi/2-0.2, db))
        time.sleep(seconds/steps)
    
    for dbase in range(0, steps):
        db = dbase/steps
        joint_servo.set_servo_angle(interp(0, math.pi/2+0.3, db))
        time.sleep(seconds/steps)

    for dbase in range(0, steps):
        db = dbase/steps
        head_servo.set_servo_angle(interp(math.pi, math.pi/2, db))
        time.sleep(seconds/steps)

    for dbase in range(0, steps):
        db = dbase/steps
        joint_servo.set_servo_angle(interp(math.pi/2+0.3, math.pi, db))
        time.sleep(seconds/steps)

    for dbase in range(0, steps):
        db = dbase/steps
        set_base_angle(interp(math.pi/2-0.2, math.pi, db))
        time.sleep(seconds/steps)

    time.sleep(5)

def reverse_procedure():
    set_base_angle(interp(math.pi/2-0.2, math.pi, 1))
    joint_servo.set_servo_angle(interp(math.pi/2+0.3, math.pi, 1))
    head_servo.set_servo_angle(interp(math.pi, math.pi/2, 1))
    time.sleep(5)

    print("Reversing...")

    steps = 200
    seconds = 15

    # Reverse the order of the loops and interpolate from end to start
    for dbase in range(steps-1, -1, -1):
        db = dbase/steps
        set_base_angle(interp(math.pi/2-0.2, math.pi, db))
        time.sleep(seconds/steps)

    for dbase in range(steps-1, -1, -1):
        db = dbase/steps
        joint_servo.set_servo_angle(interp(math.pi/2+0.3, math.pi, db))
        time.sleep(seconds/steps)

    for dbase in range(steps-1, -1, -1):
        db = dbase/steps
        head_servo.set_servo_angle(interp(math.pi, math.pi/2, db))
        time.sleep(seconds/steps)

    for dbase in range(steps-1, -1, -1):
        db = dbase/steps
        joint_servo.set_servo_angle(interp(0, math.pi/2+0.3, db))
        time.sleep(seconds/steps)

    for dbase in range(steps-1, -1, -1):
        db = dbase/steps
        set_base_angle(interp(0, math.pi/2-0.2, db))
        time.sleep(seconds/steps)

    time.sleep(5)

def scan_down_opp():
    set_base_angle(math.pi/2)
    time.sleep(2)
    joint_servo.set_servo_angle(math.pi/2+0.5)
    head_servo.set_servo_angle(math.pi)
    time.sleep(15)

    print("Starting...")
    
    steps = 200
    images = 10
    seconds = 25
    for dbase in range(0, steps):
        db = dbase/steps
        set_base_angle(interp(math.pi/2, math.pi, db))
        joint_servo.set_servo_angle(interp(math.pi/2+0.5, 0.3, db))
        head_servo.set_servo_angle(interp(math.pi, -math.pi, db))
        if db % (1/images) == 0:
            camera.take_image("images/image_{}.jpg".format(int(db*images)))
            print("Captured image {}".format(int(db*images)))
        time.sleep(seconds/steps)

if __name__ == "__main__":
    # reverse_procedure()
    # scan_down()
    scan_down_opp()