import os
from setuptools import find_packages, setup

package_name = 'c2_serial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files:
        (os.path.join('share', package_name, 'launch'), ['launch/launch_all.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sadhy',
    maintainer_email='sadhy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'c2_serial = c2_serial.c2_serial:main',
            'c2_input = c2_serial.c2_input:main',
            'c2_logger = c2_serial.c2_logger:main',
        ],
    },
)
