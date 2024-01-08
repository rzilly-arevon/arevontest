# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:37:37 2024

@author: RyanZilly
"""

from setuptools import setup 
  
setup( 
    name='arevonpytestname', 
    version='0.1', 
    description='Libaries for solar energy reporting', 
    author='Ryan Zilly', 
    author_email='rzilly@arevonenergy.com', 
    packages=['my_package'], 
    install_requires=[ 
        'numpy', 
        'pandas', 
    ], 
) 