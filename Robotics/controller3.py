import math
import random

def getAngle(xIn, yIn):
    answer = round(math.atan2(xIn, yIn) * 180/ math.pi)
    if answer < 0:
        answer = 360 + answer
    return answer

def motor1(angleIn):
    """
    angleIn is measured in degrees
    """
    return -1 * math.sin(math.radians(angleIn-60))

def motor2(angleIn):
    """
    angleIn is measured in degrees
    """
    return math.cos(math.radians(angleIn - 30))

def motor3(angleIn):
    """
    angleIn is measured in degrees
    """
    return math.cos(math.radians(angleIn))

def drive(theta):
    print(theta, round(motor1(theta), 3), round(motor2(theta), 3), round(motor3(theta), 3))

if __name__ == '__main__':
    for i in range(25):
        getX = random.randint(-5, 5)
        getY = random.randint(-5, 5)
        print(getX, getY, end=" ")
        drive(getAngle(getX, getY))
