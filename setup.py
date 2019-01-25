#!/usr/bin/env python

from mp import version
from distutils.core import setup

setup(name='ESPBlocks',
      version=version.FULL,
      description='A simple editor and blockly for ESP8266 Or ESP32 and WiPy Micropython devices.',
      author='Juwan',
      author_email='junhuanchen@qq.com',
      url='https://github.com/junhuanchen/ESPBlocks',
      install_requires=['pyserial', 'colorama', 'websocket_client'],
      scripts=['editor'],
      keywords=['micropython', 'ESPBlocks', 'blockly', 'development'],
      classifiers=[],
)
