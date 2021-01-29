from setuptools import setup

# read the contents of your README file
from os import path
work_dir = path.abspath(path.dirname(__file__))
with open(path.join(work_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pertchart',
  packages = ['pertchart'],
  version = '0.5.1',
  license='MIT',
  description = 'PERT chart generator',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Sisay Chala',
  author_email = 'sisayie@gmail.com',
  url = 'https://github.com/sisayie/pertchart',
  keywords = ['pert chart', 'project plan', 'gantt'],
  install_requires=[
          'graphviz'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
