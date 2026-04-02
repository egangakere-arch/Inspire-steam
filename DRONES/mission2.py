from pysimverse import drone
import time

drone = drone()
drone.connect()

drone.takeoff() # Distance is in cm

left_right = 6
foward_back = 10
up_down = 0

# in degrees
yaw = 0

while True:
    left_right = left_right,
    foward_back = foward_back,
    up_down = up_down,  
    yaw = yaw   