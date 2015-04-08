#!/usr/bin/env python

from distutils.core import setup

setup(name='Example-Boto-Project',
      version='1.0',
      description='An example project which uses Boto',
      long_description='An example project which uses Boto',
      author='Waldemar Zurowski',
      license='GPL3',
      url='https://github.com/wzur/example-boto-project',
      packages=['example-boto'],
      package_dir={'': 'src'},
      scripts=['src/ExampleBoto.py'],
      requires=['requests', 'json', 'argparse', 'boto'],
      platforms=['unix'],
      )

