# ----------------------------------------------------------------------------- #
#                                                                               #        
#    Project:        Right Arcade Control                                       #
#    Module:         main.py                                                    #
#    Author:         Connor Abraham                                             #
#    Created:        Fri Sept 5 2025                                            #
#    Description:                                                               #
#                                                                               #                                                                          
#    Configuration:  V5 Clawbot (Individual Motors)                             #
#                    Controller                                                 #
#                    Claw Motor in Port 3                                       #
#                    Arm Motor in Port 8                                        #
#                    Left Motor in Port 1                                       #
#                    Right Motor in Port 10                                     #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
l1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
r1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
l2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
r2 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)

# Begin project code
# Main Controller loop to set motors to controller axis postiions
while True:
    left_motor.set_velocity((controller_1.axis2.position() + controller_1.axis1.position()), PERCENT)
    right_motor.set_velocity((controller_1.axis2.position() - controller_1.axis1.position()), PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    wait(5, MSEC)
