from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='taskaty',
    version='0.1.0',
    description='A Simple Command-Line Task-App Written In Python',
    author='Faris Sammour',
    install_requires=['tabulate'],
    entry_points={
        'console_scripts': [
            'taskaty=taskaty:main',
        ]
    }




)
