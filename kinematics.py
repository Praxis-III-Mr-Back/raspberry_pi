import math
import numpy as np
import matplotlib.pyplot as plt

class Kinematics:
    # https://robotacademy.net.au/lesson/inverse-kinematics-for-a-2-joint-robot-arm-using-geometry/

    def __init__(self, length):
        self.length = length

    def check_arm(q1, q2):
        joint = get_joint_pos(q1, q2)
        return joint[1] >= 1 # Check if joint is above y=1

    def get_q1(q2):
        return math.atan(y/x) - math.atan(l*math.sin(q2)/(l+l*math.cos(q2)))

    def get_joint_pos(q1, q2):
        return self.length * math.cos(q1), self.length * math.sin(q1)

    def get_head_pos(q1, q2):
        return self.length * math.cos(q1) + self.length * math.cos(q1+q2), self.length * math.sin(q1) + self.length * math.sin(q1+q2)

    def get_angles(x, y):
        q2 = math.acos((x**2 + y**2 - 2*self.length**2) / (2 * self.length**2))
        q1 = get_q1(q2)
        a = q2 - math.pi

        best_q2 = None
        for test_q2 in [q2, -q2]:
            q1 = get_q1(test_q2)
            if check_arm_1(joint2[0], joint2[1]) and check_arm_2(joint3[0], joint3[1]):
                best_q2 = test_q2
                break

        q2 = best_q2
        q1 = get_q1(q2)

    def plot(q1, q2):
        joint = get_joint_pos(q1, q2)
        head = get_head_pos(q1, q2)
        plt.plot([0, head[0], joint3[0]], [0, joint[1], head[1]])
        plt.plot(0, 0, 'bo')
        plt.plot(joint[0], joint[1], 'bo')
        plt.plot(head[0], head[1], 'bo')
        plt.plot(x, y, 'ro')
        plt.xlim(-6, 6)
        plt.ylim(-6, 6)
        plt.show()

if __name__ == "__main__":
    k = Kinematics(2)
    q1, q2 = k.get_angles(3, 3)
    k.plot(q1, q2)