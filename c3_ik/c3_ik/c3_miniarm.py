import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class C3MiniArmNode(Node):
    def __init__(self):
        super().__init__('c3_miniarm')
        self.declare_parameter('L1', 14.0)
        self.declare_parameter('L2', 15.5)
        self.L1 = self.get_parameter('L1').value
        self.L2 = self.get_parameter('L2').value

        # Subscriber: target coordinates
        self.sub = self.create_subscription(
            Vector3,
            '/miniarm/target',
            self.cb_target,
            10
        )
        # Publisher: joint angles
        self.pub = self.create_publisher(
            Vector3,
            '/miniarm/angles',
            10
        )

        self.get_logger().info(f'Node initialized with L1={self.L1} cm, L2={self.L2} cm')

    def cb_target(self, msg: Vector3):
        x, y = msg.x, msg.y
        r = math.hypot(x, y)

        # Reachability check
        if r < abs(self.L1 - self.L2) or r > (self.L1 + self.L2):
            self.get_logger().error(f'Target unreachable (r={r:.2f} cm)')
            return

        # Compute elbow angle d2
        cos_theta2 = (self.L1**2 + self.L2**2 - r**2) / (2 * self.L1 * self.L2)
        theta2 = math.acos(max(-1.0, min(1.0, cos_theta2)))

        # Compute shoulder angle d1
        alpha = math.atan2(y, x)
        cos_beta = (self.L1**2 + r**2 - self.L2**2) / (2 * self.L1 * r)
        beta = math.acos(max(-1.0, min(1.0, cos_beta)))
        theta1 = alpha - beta

        # Convert to degrees
        theta1_deg = math.degrees(theta1)
        theta2_deg = math.degrees(theta2)

        # Publish
        out = Vector3()
        out.x = float(theta1_deg)
        out.y = float(theta2_deg)
        out.z = 0.0  # unused
        self.pub.publish(out)

        self.get_logger().info(
            f'Computed angles : d1={theta1_deg:.2f} degrees, d2={theta2_deg:.2f} degrees'
        )

def main(args=None):
    rclpy.init(args=args)
    node = C3MiniArmNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
