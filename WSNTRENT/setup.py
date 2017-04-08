try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project created for WSN, 4 micromice will communicate through CORE',
    'author': 'Nicolas Burgess, Vivek Patel, Brian Lee, Trent Walls',
    'author_email': 'nrb45408@uga.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'MICROMOUSE'
}

setup(**config)
