from distutils.core import setup
setup(
  name = 'pertchart',
  packages = ['pertchart'],
  version = '0.3',
  license='MIT',
  description = 'PERT chart generator',
  author = 'Sisay Chala',
  author_email = 'sisayie@gmail.com',
  url = 'https://github.com/sisayie/pertchart',
  download_url = 'https://github.com/sisayie/pertchart/archive/v_03.tar.gz',
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
