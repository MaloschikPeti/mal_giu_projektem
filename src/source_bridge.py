import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class BatmanDraw(Node):
    def __init__(self):
        super().__init__('batman_draw')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.count_ = 0
        self.get_logger().info("Drawing a Batman logo in Turtlesim.")
        self.loop()

    def publish_message(self, fwd, turn):
        msg = Twist()
        msg.linear.x = fwd
        msg.angular.z = turn
        self.count_ += 1
        self.get_logger().info(f"Step {self.count_}. Speed: {fwd:.1f}, Turn: {turn:.1f}")
        self.publisher_.publish(msg)
        time.sleep(2)  # Delay for 2 seconds

    def loop(self):
        self.get_logger().info("Loop started.")
        time.sleep(2)  # Delay for 2 seconds
        
        self.publish_message(0.0, math.pi / 2)  # Rotate 90 degrees
        self.publish_message(math.pi / 2, -math.pi / 2)  # Turn right and move forward
        self.publish_message(0.0, math.pi / 2)
        self.publish_message(math.pi / 2, -math.pi / 2)  # Turn right and move forward
        self.publish_message(0.0, math.pi)  # Rotate 180 degrees
        self.publish_message(4.06, 0.0)  # Move forward

        self.publish_message(0.0, math.pi)  # Rotate
        self.publish_message(math.pi / 2, -math.pi / 2)  # Turn right and move forward
        self.publish_message(0.0, math.pi / 2)
        self.publish_message(math.pi / 2, -math.pi / 2)  # Turn right and move forward
        self.publish_message(0.0, math.pi)  # Rotate

        self.get_logger().info("Program finished")
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = BatmanDraw()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

