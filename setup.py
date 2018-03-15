#from distutils.core import setup
from setuptools import setup

descrition0 = 'Estimation of canopy attributes from digital cover photography'

# from pipreqs
install_requires0 = [
    "pandas>=0.20.1",
    "scipy>=0.19.1",
    "numpy>=1.11.0",
    "scikit_image>=0.13.1",
    "rawpy>=0.10.1",
    "PyYAML>=3.12",
    "xlwt>=1.3.0"
]

entry_points0 = {
    'console_scripts': [
        'caco_cli = caco.caco_cli:main',
    ],
    'gui_scripts': [
    ]
}



classifiers0 = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
  name                 = 'caco',
  description          = descrition0,
  version              = '0.02.4',
  license              = 'MIT',
  install_requires     = install_requires0,
  author               = 'Alessandro Alivernini',
  packages             = ['caco'],
  entry_points         = entry_points0,
  author_email         = 'alessandro.alivernini@crea.gov.it',
  url                  = 'https://github.com/alivernini/caco',
  download_url         = 'https://github.com/alivernini/caco/archive/v0.2.5.tar.gz',
  keywords             = ['tree', 'canopy', 'gap fraction', 'lai', 'leaf area index'],
  classifiers          = classifiers0,
  include_package_data = True  # include fiels in MANIFES.in
)
