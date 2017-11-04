import RPi.GPIO as IO
import time

DEFAULT_STEP_AMOUNT = 3
DEFAULT_DELAY = 0.01 # sleep for 10ms
GO_UP = 1
GO_DOWN = 0
GO_RIGHT = 1
GO_LEFT = 0

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
        IO.OUTPUT(TURN_DIRECTION_PIN, GO_LEFT)
    elif(turn_direction == 'right'):
        IO.OUTPUT(TURN_DIRECTION_PIN, GO_RIGHT)
    else:
        raise("ERROR: <turn> method invalid direction argument: %s" % turn_direction)

def perform_turn(turn_amount):
    for x in range(turn_amount):
        time.sleep(DEFAULT_DELAY)
        IO.OUTPUT(TURN_STEP_PIN, 1)
        time.sleep(DEFAULT_DELAY)
        IO.OUTPUT(TURN_STEP_PIN, 0)

def turn(turn_direction, turn_amount = DEFAULT_STEP_AMOUNT):
    set_turn_direction(turn_direction)
    perform_turn(turn_amount)

def set_tilt_direction(tilt_direction):
    if(tilt_direction == 'up'):
        IO.OUTPUT(TILT_DIRECTION_PIN, GO_UP)
    elif(tilt_direction == 'down'):
        IO.OUTPUT(TILT_DIRECTION_PIN, GO_DOWN)
    else:
        raise("ERROR: <tilt> method invalid direction argument: %s" % tilt_direction)

def perform_tilt(tilt_amount):
    for x in range(tilt_amount):
        time.sleep(DEFAULT_DELAY)
        IO.OUTPUT(TILT_STEP_PIN, 1)
        time.sleep(DEFAULT_DELAY)
        IO.OUTPUT(TILT_STEP_PIN, 0)

def tilt(tilt_direction, tilt_amount = DEFAULT_STEP_AMOUNT):
    set_tilt_direction(tilt_direction)
    perform_tilt(tilt_amount)

######################
# THE MAIN PROCESS:
######################
main():
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
