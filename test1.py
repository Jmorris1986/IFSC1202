#Assumptions:The robot has sensors at points A and B.
# There are actuators to control the robot’s movement.
# The PLC has inputs for the sensors and outputs for the actuators.
# Ladder Logic Program:
#Inputs:I0.0: Sensor at Point A (Part Present)
#I0.1: Sensor at Point B (Part Received)
#Outputs:
#Q0.0: Move Robot to Point A
#Q0.1: Move Robot to Point B
#Internal Memory/Flags:
#M0.0: Part Picked Up
#M0.1: Part Delivered
#Ladder Logic Steps:
#|----[ I0.0 ]-------------------------( M0.0 )----|
#|    (Sensor at A)                  (Part Picked) |

#|----[ M0.0 ]-------------------------( Q0.0 )----|
#|    (Part Picked)                 (Move to B)   |

#|----[ I0.1 ]-------------------------( M0.1 )----|
#|    (Sensor at B)                (Part Delivered)|

#|----[ M0.1 ]-------------------------( Q0.1 )----|
#|    (Part Delivered)              (Move to A)   |
#Explanation:
#Line 1: When the sensor at Point A (I0.0) detects a part, it sets an internal memory bit (M0.0) indicating the part is picked up.
#Line 2: If the part is picked up (M0.0), the robot is instructed to move to Point B (Q0.0).
#Line 3: When the sensor at Point B (I0.1) detects the part, it sets another internal memory bit (M0.1), indicating the part is delivered.
#Line 4: If the part is delivered (M0.1), the robot must return to Point A (Q0.1).


I0_0 = a #(part present)
I0_1 = b #(part received)