import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64, Float64, String

class LoggerNode(Node):
    def __init__(self):
        super().__init__('c2_logger')
        self.create_subscription(Int64, '/sensor_data/value_a', self.log_value_a, 10)
        self.create_subscription(Float64, '/sensor_data/value_b', self.log_value_b, 10)
        self.create_subscription(Int64, '/sensor_data/value_c', self.log_value_c, 10)
        self.create_subscription(String, '/sensor_data/value_d', self.log_value_d, 10)

    def log_value_a(self, msg):
        self.get_logger().info(f'Value A: {msg.data}')

    def log_value_b(self, msg):
        self.get_logger().info(f'Value B: {msg.data}')

    def log_value_c(self, msg):
        self.get_logger().info(f'Value C: {msg.data}')

    def log_value_d(self, msg):
        self.get_logger().info(f'Value D: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
