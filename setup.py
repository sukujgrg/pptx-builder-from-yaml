import re
import sys
from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 4)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("Current version of python is lower than what is required (required=%s.%s)" % REQUIRED_PYTHON)


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('pptx_builder/__init__.py', encoding='utf8') as f:
    version = re.search(r'(?:__version__ = )\"(.+)\"', f.read()).group(1)

setup(
  name='pptx-builder-from-yaml',
  python_requires='>=3.4',
  version=version,
  author='Suku John George',
  author_email='sukujgrg@gmail.com',
  url='https://github.com/sukujgrg/pptx-builder-from-yaml',
  description='CLI to generate powerpoint slides from simple yaml file[s]',
  long_description=long_description,
  long_description_content_type='text/markdown',
  license='MIT',
  entry_points={
    'console_scripts': [
      'pptx-builder=pptx_builder:cli',
    ],
  },
  packages=['pptx_builder'],
  install_requires=[
    'click==7.0',
    'python-pptx==0.6.16',
    'PyYAML==3.13',
    'jsonschema==2.6.0'
  ],
  classifiers=[
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ]
)
