import sys
from setuptools import setup

VERSION = '0.0.1'

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 4)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("Current version of python is lower than what is required (required=%s.%s)" % REQUIRED_PYTHON)

setup(
  name='pptx-builder-from-yaml',
  python_requires='>=3.4',
  version=VERSION,
  author='Suku John George',
  author_email='sukujgrg@gmail.com',
  url='https://github.com/sukujgrg/pptx-builder-from-yaml',
  license='MIT',
  entry_points={
    'console_scripts': [
      'pptx-builder=scripts.gen:cli',
    ],
  },
  install_requires=[
    'click==7.0',
    'python-pptx==0.6.16',
    'PyYAML==3.13'
  ]
)
