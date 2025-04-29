from setuptools import find_packages, setup

# We're going to use these to install the launch files.
import os
from glob import glob

package_name = 'hw4'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # These lines make sure the launch files are installed
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.py'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.xml'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.yaml'))),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nathan M.',
    maintainer_email='martnat8@oregonstate.edu',


    description='HW4 for ROB 499 Robot Software Frameworks at OSU',
    license='BSD 3-Clause',


    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # A node the publishes a clamed sinwave
            'oscope = hw4.oscope:main',
            'nasa = hw4.nasa:main',
            'nasa_client = hw4.nasa_client:main',
        ],
    },
)
