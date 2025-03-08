import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class BridgeDraw(Node):
    def __init__(self):
        super().__init__('bridge_draw')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.count_ = 0
        self.get_logger().info("Drawing a bridge in Turtlesim.")
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
        
        # jobbra néz a teknős
        self.publish_message(4.0, 0.0) # négy egységet megy előre
        self.publish_message(0.0, -math.pi / 2) # 90° ot fordul jobbra
        self.publish_message(2.0, 0.0) # két egységet megy előre
        for i in range(4):
            self.publish_message(0.0, -math.pi) # 180° ot fordul jobbra
            self.publish_message(math.pi, math.pi) # jobbra fordul és megy előre egy félkört
        self.publish_message(0.0, -math.pi + 0.05) # 180° ot fordul jobbra
        self.publish_message(2.0, 0.0) # két egységet megy előre
        self.publish_message(0.0, -math.pi / 2) # 90° ot fordul jobbra
        self.publish_message(4.0, 0.0) # 4 egységet megy előre
        self.get_logger().info("Program finished")
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = BridgeDraw()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
