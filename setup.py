#!/usr/bin/env python
req=['nose','pynput','pygame']
# %%
from setuptools import setup, find_packages

setup(name='QuindarTones',
      packages=find_packages(),
      description ='Recreate tones used for in-band signaling by NASA manned missions',
      author = 'Michael Hirsch, Ph.D.',
      version = '0.1.0',
      url = 'https://github.com/scivision/quindar-tones',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      ],
      install_requires=req,
      python_requires='>=3.4',
	  )
