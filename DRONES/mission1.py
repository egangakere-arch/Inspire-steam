from pysimverse import drone
import time


#create an instance of drone
drone = drone()

drone.takeoff() # Distance is in c
drone.move_foward(280)
drone.move_backwards(360)
drone.move_right(80)
drone.move_left(80)

time.sleep(6)

drone.land()
