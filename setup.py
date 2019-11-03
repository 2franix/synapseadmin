#!/usr/bin/python3

"""
Package providing basic functionality about administering a matrix-synapse server.
"""

from setuptools import setup

setup(name='synapseadmin',
      version='1.0.0',
      description=__doc__,
      packages=['synapseadmin'],
      requires=['requests'],
      install_requires=['requests'])
