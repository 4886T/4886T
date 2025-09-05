from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()



def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

def onauton_autonomous_0():

    pass

def ondriver_drivercontrol_0():
while True:
    left_motor.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
    right_motor.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    wait(5, MSEC)

# create a function for handling the starting and stopping of all autonomous tasks
def auton():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def driver():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition(driver, auton)

when_started1()

