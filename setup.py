from setuptools import find_packages, setup

package_name = 'hw4'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'oscope = hw2.oscope:main',
        ],
    },
)
