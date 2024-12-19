#!/usr/bin/env python3

import rclpy
from rclpy.parameter import Parameter, ParameterType
from harpia_msgs.srv import GeneratePath
from geometry_msgs.msg import PoseStamped
from harpia_msgs.action import MoveTo
from rclpy.action import ActionClient
from plansys2_support_py.ActionExecutorClient import ActionExecutorClient


class take_image(ActionExecutorClient):
 
    def __init__(self):
        super().__init__('take_image', 1)
        self.is_new_action = True
       


    # DO NOT USE THIS ↓↓↓ FUNCTIONS TO IMPLEMENT THE ACTION 
    def finish(self, success, completion, status):
        super().finish(success, completion, status)
        self.handle_end_of_action(success, completion, status)
        self.is_new_action = True

    def do_work(self):
        if self.is_new_action:
            self.is_new_action = False
            self.handle_start_of_action()
        self.handle_action_loop()
    # DO NOT USE THIS ↑↑↑ FUNCTIONS TO IMPLEMENT THE ACTION 
    
    def handle_start_of_action(self):
        self.get_logger().info('Starting action take_image')
        self.progress_ = 0.0

            
    def handle_action_loop(self):

        self.progress_ += 0.1

        if self.progress_ < 1.0:
            self.send_feedback(self.progress_, 'Taking image...')
        else:
            self.finish(True, 1.0, 'Image successfully taken')

    def handle_end_of_action(self, success, completion, status):
        if success:
            self.get_logger().info("Action finished successfully.")
        else:
            self.get_logger().info(f"Action finished with error: {status}")

def main(args=None):
    rclpy.init(args=args)

    node = take_image()
    node.set_parameters([Parameter(name='action_name', value='take_image')])

    node.trigger_configure()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()