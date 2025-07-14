import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LEDController(Node):
    def __init__(self):
        super().__init__('led_controller')
        self.publisher = self.create_publisher(String, 'led_cmd', 10)
        self.timer = self.create_timer(1.0, self.get_input)

    def get_input(self):
        msg = String()
        msg.data = input("LED (ON/OFF): ").strip()
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = LEDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()