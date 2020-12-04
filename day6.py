# To use with: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Make sure the robot hits a wall
while front_is_clear():
    move()
turn_left()

# Follow right edge
# If right_is_clear -> turn right
# Else if right NOT clear -> go straight
# Else, turn left

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()
    

# Functions: move, turn_left, front_is_clear, 
# wall_in_front, right_is_clear, wall_on_right
