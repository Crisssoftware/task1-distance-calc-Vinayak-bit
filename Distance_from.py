#!/usr/bin/env python3
import rclpy
from rclpy.node iport Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32

class PoseDistance(Node):
    def __init__(self):
        super().__init__("pose_distance")
        self.pose_subsciber_ = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.pose_distance_ = self.create_publisher(Float32,"/turtle1/distance_from_origin",10)

    def pose_callback(self,msg : Pose):
        sqt=((msg.x)**2)+((msg.y)**2)
        dist=((sqt)**0.5)
        self.get_logger().info("Distance from origin: " + str(dist))
        self.pose_distance_.publish(Float32(data=dist))
        


def main(args=None):
    rclpy.init(args=args)
    node = PoseDistance()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()