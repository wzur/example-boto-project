#!/usr/bin/env python

from distutils.core import setup

setup(name='Example-Boto-Project',
      version='0.1',
      description='An example project which uses Boto',
      long_description='An example project which uses Boto',
      author='Waldemar Zurowski',
      author_email='wzurowski@gmail.com',
      license='GPL3',
      url='https://github.com/wzur/example-boto-project',
      package_dir={'exampleboto': 'lib/exampleboto'},
      packages=['exampleboto'],
      scripts=['scripts/ExampleBoto.py'],
      requires=['json', 'argparse', 'botocore'],
      platforms=['unix'],
      )

