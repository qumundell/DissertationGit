/*
 * File:          ned_test_vgrip.c
 * Date:
 * Description:
 * Author:
 * Modifications:
 */

/*
 * You may need to add include files like <webots/distance_sensor.h> or
 * <webots/motor.h>, etc.
 */
#include <webots/robot.h>
#include <webots/vacuum_gripper.h>
#include <webots/motor.h>
#include <stdio.h>

/*
 * You may want to add macros here.
 */
 

#define NB_STEPS 20
#define TARGETS_COUNT 10
#define TIME_STEP 64
static int time_step = 32;

/*
 * This is the main program.
 * The arguments of the main function can be specified by the
 * "controllerArgs" field of the Robot node
 */
int main(int argc, char **argv[]) {
  /* necessary to initialize webots stuff */
  wb_robot_init();
  time_step = wb_robot_get_basic_time_step();
  
  WbDeviceTag vacuum_gripper = wb_robot_get_device("vacuum gripper");
  
  
  WbDeviceTag inertial_unit = wb_robot_get_device("inertial unit");
  wb_inertial_unit_enable(inertial_unit, time_step);
  // WbDeviceTag roll_motor = wb_robot_get_device("roll motor");
  // WbDeviceTag pitch_motor = wb_robot_get_device("pitch motor");
  // WbDeviceTag yaw_motor = wb_robot_get_device("yaw motor");
  // WbDeviceTag gripper_motor = wb_robot_get_device("gripper motor");
 
  WbDeviceTag motors[7];
  motors[1] = wb_robot_get_device("joint_1");
  motors[2] = wb_robot_get_device("joint_2");
  motors[3] = wb_robot_get_device("joint_3");
  motors[4] = wb_robot_get_device("joint_4");
  motors[5] = wb_robot_get_device("joint_5");
  motors[6] = wb_robot_get_device("joint_6");
  // move arm to pick position
  wb_motor_set_position(motors[1], -1.4);
  wb_motor_set_position(motors[2], 0.7);
  wb_motor_set_position(motors[5], -0.5);
  // wait_until_target_position(inertial_unit, 0, 0, 0, -1);

  printf("Turn on vacuum gripper\n");
  wb_vacuum_gripper_turn_on(vacuum_gripper);
  wb_vacuum_gripper_enable_presence(vacuum_gripper, time_step);
  
  double slider_position = 0.0;
  
  
  while (wb_robot_step(time_step) != -1) { 
  
    wb_robot_step(time_step);
    wb_motor_set_position(motors[2], 0.0);
    wb_robot_step(100 * time_step);
    /*
     * Read the sensors :
     * Enter here functions to read sensor data, like:
     *  double val = wb_distance_sensor_get_value(my_sensor);
     */

    /* Process sensor data here */

    /*
     * Enter here functions to send actuator commands, like:
     * wb_motor_set_position(my_actuator, 10.0);
     */
  };

  /* Enter your cleanup code here */

  /* This is necessary to cleanup webots resources */
  wb_robot_cleanup();

  return 0;
}
