from setuptools import find_packages, setup

package_name = 'c1_basic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'c1_input = c1_basic.c1_input:main',
            'c1_output = c1_basic.c1_output:main',
        ],
    },
)
