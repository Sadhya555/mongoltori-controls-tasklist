import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int64, Float64
import serial

class SerialBridge(Node):
    def __init__(self):
        super().__init__('serial_bridge')
        self.serial_conn = serial.Serial('COM4', 9600, timeout=1)

        self.subscription = self.create_subscription(
            String, 'led_cmd', self.send_cmd, 10
        )

        self._topic_publishers = {
            'A': self.create_publisher(Int64, '/sensor_data/value_a', 10),
            'B': self.create_publisher(Float64, '/sensor_data/value_b', 10),
            'C': self.create_publisher(Int64, '/sensor_data/value_c', 10),
            'D': self.create_publisher(String, '/sensor_data/value_d', 10),
        }

        self.timer = self.create_timer(0.1, self.read_serial)

    def send_cmd(self, msg):
        command = msg.data.strip()
        if command in ["ON", "OFF"]:
            self.serial_conn.write((command + '\n').encode())

    def read_serial(self):
        while self.serial_conn.in_waiting:
            line = self.serial_conn.readline().decode().strip()
            print(line)
            if ':' in line:
                prefix, val = line.split(':', 1)
                if prefix == 'A':
                    self._topic_publishers['A'].publish(Int64(data=int(val)))
                elif prefix == 'B':
                    self._topic_publishers['B'].publish(Float64(data=float(val)))
                elif prefix == 'C':
                    self._topic_publishers['C'].publish(Int64(data=int(val)))
                elif prefix == 'D':
                    self._topic_publishers['D'].publish(String(data=val))

def main(args=None):
    rclpy.init(args=args)
    node = SerialBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
