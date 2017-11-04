import RPi.GPIO as IO
import time

DEFAULT_STEP_AMOUNT = 3
DEFAULT_DELAY = 0.01 # sleep for 10ms
GO_UP = 1
GO_DOWN = 0
TURN_RIGHT = 1
TURN_LEFT = 0

# Ignore the warnings when pins are busy
# and proceed with the program.
IO.setwarnings(False)

# Use pin numbers not names
IO.setmode (IO.BCM)

########################
### PIN DEFINITIONS: ###
########################
# TILT-MOTOR:
TILT_STEP_PIN = 3
TILT_DIRECTION_PIN = 5
IO.setup(TILT_STEP_PIN, IO.OUT)
IO.setup(TILT_DIRECTION_PIN, IO.OUT)

# TURNING MOTOR:
TURN_STEP_PIN = 7
TURN_DIRECTION_PIN = 8
IO.setup(TURN_STEP_PIN, IO.OUT)
IO.setup(TURN_DIRECTION_PIN, IO.OUT)
########################

def set_turn_direction(turn_direction):
    if(turn_direction == 'left'):
        print("Turnign left...")
        IO.output(TURN_DIRECTION_PIN, TURN_LEFT)
    elif(turn_direction == 'right'):
        print("Turning right...")
        IO.output(TURN_DIRECTION_PIN, TURN_RIGHT)
    else:
        raise("ERROR: <turn> method invalid direction argument: %s" % turn_direction)

def perform_turn(turn_amount):
    print("Performing turn:")
    for x in range(turn_amount):
        print("Turn: ", x)
        time.sleep(DEFAULT_DELAY)
        IO.output(TURN_STEP_PIN, 1)
        time.sleep(DEFAULT_DELAY)
        IO.output(TURN_STEP_PIN, 0)

def turn(turn_direction, turn_amount = DEFAULT_STEP_AMOUNT):
    print("TURN")
    set_turn_direction(turn_direction)
    perform_turn(turn_amount)

def set_tilt_direction(tilt_direction):
    if(tilt_direction == 'up'):
        print("Tilting up...")
        IO.output(TILT_DIRECTION_PIN, GO_UP)
    elif(tilt_direction == 'down'):
        print("Tilding down...")
        IO.output(TILT_DIRECTION_PIN, GO_DOWN)
    else:
        raise("ERROR: <tilt> method invalid direction argument: %s" % tilt_direction)

def perform_tilt(tilt_amount):
    print("Perform tilt:")
    for x in range(tilt_amount):
        print("Tilt: ", x)
        time.sleep(DEFAULT_DELAY)
        IO.output(TILT_STEP_PIN, 1)
        time.sleep(DEFAULT_DELAY)
        IO.output(TILT_STEP_PIN, 0)

def tilt(tilt_direction, tilt_amount = DEFAULT_STEP_AMOUNT):
    print("TILT")
    set_tilt_direction(tilt_direction)
    perform_tilt(tilt_amount)

######################
# THE MAIN PROCESS:
######################
def main():
    tilt('up', 500)
    # TURNING LOGIC:
    # if image processing says drone goes left:
        # turn('left')
    # if image processing says drone goes right:
        # turn('right')

    # TILT LOGIC:
    # if image processing says drone incoming:
        # tilt('up')
    # elsif image processing says drone leaving:
        # tilt('down')
main()
