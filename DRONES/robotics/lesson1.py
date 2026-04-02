from robodk import robolink, robomath

# Connect to RoboDK
RDK = robolink.Robolink()

# Select a robot (opens a selection dialog if multiple robots are loaded)
robot = RDK.ItemUserPick('Select a robot', robolink.ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No robot selected or available.")

# Define a target position (x, y, z in mm, rotations in degrees)
target_pose = robomath.transl(300, 0, 500) * robomath.rotz(90 * robomath.pi / 180)

# Move the robot
robot.MoveJ(target_pose)  # Joint move
robot.MoveL(target_pose)  # Linear move

print("Movement complete.")
