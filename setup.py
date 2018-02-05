#!/usr/bin/env python
install_requires = ['pygame','numpy']
tests_require = ['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='quindar_tones',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/quindar-tones',
      long_description=open('README.rst').read(),
      description='Play Nextel, Quindar, Tone Remote tones',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
      python_requires='>=2.7',
	  )

