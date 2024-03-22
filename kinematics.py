import math
import numpy as np
import matplotlib.pyplot as plt

class Kinematics:
    # https://robotacademy.net.au/lesson/inverse-kinematics-for-a-2-joint-robot-arm-using-geometry/

    def __init__(self, length):
        self.length = length

    def check_arm(self, q1, q2):
        joint = self.get_joint_pos(q1, q2)
        return joint[1] >= 1 # Check if joint is above y=1

    def get_q1(self, x, y, q2):
        return math.atan(y/x) - math.atan(self.length*math.sin(q2)/(self.length+self.length*math.cos(q2)))

    def get_joint_pos(self, q1, q2):
        return self.length * math.cos(q1), self.length * math.sin(q1)

    def get_head_pos(self, q1, q2):
        return self.length * math.cos(q1) + self.length * math.cos(q1+q2), self.length * math.sin(q1) + self.length * math.sin(q1+q2)

    def get_angles(self, x, y):
        q2 = math.acos((x**2 + y**2 - 2*self.length**2) / (2 * self.length**2))
        q1 = self.get_q1(x, y, q2)
        a = q2 - math.pi

        best_q2 = None
        for test_q2 in [q2, -q2]:
            q1 = self.get_q1(x, y, test_q2)
            if self.check_arm(q1, q2):
                best_q2 = test_q2
                break

        return self.get_q1(x, y, best_q2), best_q2

    def plot(self, q1, q2):
        joint = self.get_joint_pos(q1, q2)
        head = self.get_head_pos(q1, q2)
        plt.plot([0, joint[0], head[0]], [0, joint[1], head[1]])
        plt.plot(0, 0, 'bo')
        plt.plot(joint[0], joint[1], 'bo')
        plt.plot(head[0], head[1], 'bo')
        plt.xlim(-6, 6)
        plt.ylim(-6, 6)
        plt.show()
        plt.savefig("plot.png")

if __name__ == "__main__":
    k = Kinematics(4)
    q1, q2 = k.get_angles(2, 2)
    print(math.degrees(q1), math.degrees(q2))
    k.plot(q1, q2)