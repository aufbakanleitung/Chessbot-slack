"""
Hello World app for running Python apps on Bluemix
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='python-chessbot-slack',
    version='1.0.0',
    description='Chessbot running in Python on Bluemix',
    long_description= 'A slackbot that will keep score of the chessgames played at the CIC, Groningen /n'
                      'It uses Google sheets as a database, making it hella slow (about 1 operation/sec)',
    url='https://github.com/aufbakanleitung/Chessbot-slack',
    license='Apache-2.0'
)
