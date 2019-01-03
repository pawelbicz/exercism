import random
import string


class Robot(object):
    def __init__(self):
        self.names_table = []
        self.reset()

    def robot_name(self):
        n = ''.join(random.choice(string.ascii_uppercase) for i in range(2)) + ''.join(random.choice(string.digits) for i in range(3))
        for i in self.names_table:
            if n == i:
                self.robot_name()
        return n

    def reset(self):
        self.name = self.robot_name()

n = Robot().name
print(n)
